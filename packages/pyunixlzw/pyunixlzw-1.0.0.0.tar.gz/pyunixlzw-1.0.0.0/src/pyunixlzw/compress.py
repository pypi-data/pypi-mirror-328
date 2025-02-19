 ################################################################################
#   Author:         Justin Berthelot                                            #
#   Date:           02/17/2025                                                  #
#   Description:    LZW compression in "pure" python.                           #
################################################################################

def check_clear(last_table_entry_index, cur_bit_len, max_bit_len):
    """Implements the function to check if we need to output a clear code.
    
    **NOTE**: This does not follow the same logic as the `ncompress` implementation
    
    Return:
    - `bool`
        - Determination on need for clear code
    """
    return last_table_entry_index == (1 << cur_bit_len) and cur_bit_len >= max_bit_len

def get_next_byte(output_code, output_int_buf, remaining_bit_count, cur_bit_len):
    """Returns the next output byte alongside buffer tracking information.
    
    Parameters:
    - `int` output_code
        - The code from our code table that we want to add to our compressed stream
    - `int` output_int_buf
        - The current single byte buffer that may contain bits from a previous output 
          code
    - `int` remaining_bit_count
        - The remaining bits that we need to fill in the current single byte buffer
    - `int` cur_bit_len
        - The current bit length for codes in our table

    Return:
    - `tuple[list[int], int, int]`
        - The list of bytes that can be output to the compressed stream from the given code
        - The updated single byte buffer that contains the leftover bits 
        - The updated remaining bits needed to fill the rest of the single byte buffer
    """
    # Since bit length > 8, we will always be able to output at least one byte
    output_bytes = [
        # Add bits that already existed in our output buffer to...
        output_int_buf + (
            # our output code bit shifted by the bits that have already been read...
            (output_code << (8 - remaining_bit_count)) & 
            # masked to only include the bits that we need to read
            (((2 ** (8 - remaining_bit_count)) - 1) ^ 0xff)
        )
    ]
    # Shift out the bits we have already read
    output_code >>= remaining_bit_count
    # Update our remaining bit count
    remaining_bit_count = cur_bit_len - remaining_bit_count

    # Continue adding bytes to our output byte buffer while we can
    while remaining_bit_count > 8:
        # Append the last 8 LSBs of our output code to the existing output byte buffer
        output_bytes.append(output_code & 0xff)
        # Shift out 8 bits
        output_code >>= 8
        # Update our remaining bit count
        remaining_bit_count -= 8
    
    # We can read one more byte before outputting our byte buffer
    if remaining_bit_count == 8:
        # Add the remaining bits of the output_code as a full byte to our byte buffer
        output_bytes.append(output_code)
        # Clear the single byte buffer
        output_int_buf = 0
    # Leverage single byte buffer
    else:
        # Put left over bits into the single byte buffer
        output_int_buf = output_code & (2 ** (remaining_bit_count) - 1)
        # Update for bits we will need to continue reading later
        remaining_bit_count = 8 - remaining_bit_count

    return (output_bytes, output_int_buf, remaining_bit_count)

def compress(decompressed_data, init_bit_len=9, max_bit_len=16, block_mode=True):
    """Implements LZW compress.
    
    Parameters:
    - `bytes` decompressed_data
        - The decompressed input data that we plan to decompress
    - `int` init_bit_len
        - The initial bit length of code entries in the code table
    - `int` max_bit_len
        - The maximum bit length of code entries in the code table
    - `bool` block_mode
        - Determines whether we include the CLEAR code or not

    Return:
    - `bytes`
        - The compressed output of our input data
    """

    # Initialize variables
    cur_bit_len = init_bit_len
    cur_byte = 0
    output_int_buf = 0
    remaining_bit_count = 8
    largest_char_size = 1
    block_start = 3
    # Save the length of the decompressed data as we will use this throughout the compression
    decompressed_data_len = len(decompressed_data)

    # Make sure no one made a silly mistake putting an impossible max bit length
    if max_bit_len > 127:
        print("Max bit length too large to process!")
        return None

    # Start our compressed output with the two magic bytes and flag byte from the
    #  max bit length and block mode
    compressed_output = [0x1f, 0x9d, max_bit_len | 0x80 if block_mode else 0x00]

    # Return header with empty data
    if decompressed_data_len == 0:
        return bytes(bytearray(compressed_output))

    # Initialize our code table (include CLEAR code)
    code_table = {i.to_bytes(1, 'big') : i for i in range(256)}
    if block_mode:
        # Key as a string to ensure we don't accidentally use this as a match
        code_table['CLEAR'] = 256
        last_table_entry_index = 257
    else:
        last_table_entry_index = 256

    # Loop over the decompressed data
    while cur_byte < decompressed_data_len:

        # Check if we need to output a CLEAR code
        if check_clear(last_table_entry_index, cur_bit_len, max_bit_len):
            # Output the CLEAR code
            code_output_bytes, output_int_buf, remaining_bit_count = get_next_byte(
                code_table['CLEAR'], 
                output_int_buf, 
                remaining_bit_count, 
                cur_bit_len
            )
            compressed_output += code_output_bytes

            # Add bytes to get to the required boundary
            compressed_output += [0x00] * ((16 - ((len(compressed_output) - block_start) % 16)) % 16)
            # Update the start index of the next compressed block
            block_start = len(compressed_output)

            # Reset the table
            cur_bit_len = 9
            code_table = {i.to_bytes(1, 'big') : i for i in range(256)}
            code_table['CLEAR'] = 256
            last_table_entry_index = 257
            largest_char_size = 1

        # Initialize the code index to verify we found a code in our table
        code_idx = None
        # Determine the largest buffer size we need to read (optimization)
        if (cur_byte + largest_char_size) < decompressed_data_len:
            max_idx = (cur_byte + largest_char_size)
        else:
            max_idx = decompressed_data_len
        # Find the longest match
        for end_byte in range(max_idx, cur_byte, -1):
            # Code to search for
            search_code = decompressed_data[cur_byte:end_byte]
            # Match found
            if code_table.get(search_code) is not None:
                # Get the code index
                code_idx = code_table.get(search_code)
                # Skip over codes that are larger than the allowed maximum bit length
                if code_idx > (2 ** (max_bit_len) - 1):
                    continue
                # Get the next code to add to our sliding window
                new_code = decompressed_data[cur_byte:end_byte + 1]
                # Update the largest_char_size to speed up processing
                if len(new_code) > largest_char_size:
                    largest_char_size = len(new_code)
                # Update the current byte
                cur_byte = end_byte
                break

        # Code was not found (something went very wrong)
        if code_idx is None:
            print(f"Could not find code at {cur_byte}!")
            return None
        
        # Get the next output byte and update byte buffer details
        code_output_bytes, output_int_buf, remaining_bit_count = get_next_byte(
            code_idx, 
            output_int_buf, 
            remaining_bit_count, 
            cur_bit_len
        )

        # Add the output bytes to the running compressed output
        compressed_output += code_output_bytes

        # Handle code bit length increase
        if last_table_entry_index == (1 << cur_bit_len) and cur_bit_len < max_bit_len:
            cur_bit_len += 1

        # Only update the table if we still have data to process
        if cur_byte < decompressed_data_len:
            code_table[new_code] = last_table_entry_index
            last_table_entry_index += 1

    # Add the last buffer byte
    if (remaining_bit_count % 8) != 0:
        compressed_output.append(output_int_buf)

    return bytes(bytearray(compressed_output))
