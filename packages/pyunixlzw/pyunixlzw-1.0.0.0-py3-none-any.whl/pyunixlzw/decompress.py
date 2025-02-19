 ################################################################################
#   Author:         Justin Berthelot                                            #
#   Date:           02/17/2025                                                  #
#   Description:    LZW decompression in "pure" python.                         #
################################################################################

def flush(cur_byte, block_start_index, cur_bit_len, input_data_len):
    """Moves to the next clean (bit size * byte) boundary and clears the buffer 
    and remaining bits.

    Parameters:
    - `int` cur_byte
        - The current byte index within the compressed output
    - `int` block_start_index
        - The current start of the compressed block data within the compressed output
    - `int` cur_bit_len
        - The current bit length for entries in the table
    - `int` input_data_len
        - The length of the full compressed input data

    Return:
    - `tuple[int, int, int, int]`
        - The new current byte index in our compressed output
        - The new block start index
        - The remaining bit count which will always be 0 as we reset it
        - The single byte buffer which will always be 0 as we reset it
    """
    # Get the number of bytes to get to the next (cur_bit_len * byte) boundary
    bytes_from_boundary = (cur_bit_len - ((cur_byte - block_start_index) % cur_bit_len)) % cur_bit_len

    # If we are not at the boundary, we need to move the current byte to it
    if bytes_from_boundary != cur_bit_len:
        # Not enough bytes to add to continue processing; simply exit
        if bytes_from_boundary >= input_data_len - cur_byte:
            return None
        # Move to that byte
        cur_byte += bytes_from_boundary
    
    # Update the block start index and return all the data
    block_start_index = cur_byte
    return (cur_byte, block_start_index, 0, 0)

def decompress(compressed_data, init_bit_len=9, max_bit_len=16):
    """Implements LZW decompress.
    
    Parameters:
    - `bytes` compressed_data
        - The compressed input data that we plan to decompress
    - `int` init_bit_len
        - The initial bit length of code entries in the code table
    - `int` max_bit_len
        - The maximum bit length of code entries in the code table

    Return:
    - `bytes` | None
        - The decompressed output of our input data
    """

    # Data must be at least 3 bytes in size
    if len(compressed_data) < 3:
        print('Data too short to process!')
        return None
    # Data must begin with magic header \x1f\x9d
    elif (compressed_data[0] != 0x1f) or (compressed_data[1] != 0x9d):
        print('Invalid magic bytes!')
        return None
    # Data of size 3 is empty data
    elif len(compressed_data) == 3:
        return b''
    # Data of size 4 is invalid
    elif len(compressed_data) == 4:
        print('Stream ended prior to processing!')
        return None

    # Save the length of the compressed data as we will use this throughout the decompression
    compressed_data_len = len(compressed_data)

    # For a given table entry key, store a tuple value of the LZW prefix and suffix
    prefix_suffix_map = {}
    # We have already parsed the magic header and are now at the 3rd byte
    cur_byte = 2

    # Running bit size for table entries and associated bitmask
    cur_bit_len = init_bit_len
    bitmask = (2 ** cur_bit_len) - 1

    # Get the maximum bit size from the header
    max_bit_len = int(bin(compressed_data[cur_byte])[2:][-5:], 2)

    # Adds the clear code to the table to provide an option to flush tables
    block_mode_flag = int(bin(compressed_data[cur_byte])[2:][0])
    # 257th entry if we need clear code; 256th entry if we do not need the clear code
    last_table_entry_index = 256 if block_mode_flag else 255

    # Move to the next byte
    cur_byte += 1

    # Get the first code by reading the next two bytes and masking it
    buf = compressed_data[cur_byte] + (compressed_data[cur_byte + 1] << 8)
    code = buf & bitmask
    prev_code = last_code = code
    # We read 16 bits
    remaining_bit_count = 16
    # Error check
    if code > 255:
        print('First code must be the size of a byte!')
        return None

    # Safe to start our output buffer
    decompressed_output = [code]

    # Remove the already processed bits from our running buffer and update the
    #  remaining bit count for how many bits are left in our buffer
    buf >>= cur_bit_len
    remaining_bit_count -= cur_bit_len

    # Move to the next entry
    cur_byte += 2

    # start of compressed data
    block_start_index = 3

    while cur_byte < compressed_data_len:

        # Code bit length increment required
        if (last_table_entry_index >= bitmask) and (cur_bit_len < max_bit_len):
            # Flush the input
            ret = flush(cur_byte, block_start_index, cur_bit_len, compressed_data_len)
            # Not enough bytes to add to continue processing; simply exit loop
            if ret is None:
                break
            # Update values based on the flush
            cur_byte, block_start_index, remaining_bit_count, buf = ret

            # Increment running bit size for table entries and associated bitmask
            cur_bit_len += 1
            bitmask = (bitmask << 1) + 1

            # Simply fail if we exceed the maximum number of codes allowed
            if cur_bit_len > max_bit_len:
                print(f"Code entry size exceeds max bit length ({cur_bit_len})!")
                return None

        # Update our buffer by adding the next byte shifted by the necessary bits
        #  to our existing buffer data
        buf += compressed_data[cur_byte] << remaining_bit_count
        # Update our remaining bit count as we added a byte to our buffer
        remaining_bit_count += 8

        # We need extra bits to reach the bit length
        if remaining_bit_count < cur_bit_len:
            # No bits remaining to read
            if cur_byte == compressed_data_len:
                print('Stream ended prematurely!')
                return None
            # Update our buffer by adding the next byte shifted by the necessary bits
            #  to our existing buffer data
            if (cur_byte + 1) < len(compressed_data):
                buf += compressed_data[cur_byte + 1] << remaining_bit_count
                # Update our remaining bit count as we added a byte to our buffer
                remaining_bit_count += 8
                # Move to the next entry
                cur_byte += 2
            else:
                cur_byte += 1
        else:
            # Move to the next entry
            cur_byte += 1
        
        # Get the next code by applying the bitmask to our buffer
        temp = buf & bitmask

        # Remove the already processed bits from our running buffer and update the
        #  remaining bit count for how many bits are left in our buffer
        buf >>= cur_bit_len
        remaining_bit_count -= cur_bit_len

        # CLEAR code with block_mode
        if (temp == 256) and block_mode_flag:
            # Flush the input
            ret = flush(cur_byte, block_start_index, cur_bit_len, compressed_data_len)
            # Not enough bytes to add to continue processing; simply exit loop
            if ret is None:
                break
            # Update values based on the flush
            cur_byte, block_start_index, remaining_bit_count, buf = ret
            
            # Reset running bit size for table entries, associated bitmask, and 
            #  last table entry index
            cur_bit_len = init_bit_len
            bitmask = (2 ** cur_bit_len) - 1
            last_table_entry_index = 255

            # Move to the next entry
            continue

        # Buffer for matched codes
        matched_code_buf = []

        # Bad stream case
        if (prev_code > last_table_entry_index) and (temp > last_table_entry_index):
            print('Invalid code! (Code reuse with invalid index)')
            return None
        # Reuse last match
        elif (temp > last_table_entry_index):
            # Add the last code to our matched code buffer
            matched_code_buf.insert(0, last_code)
            # Update the current code
            code = prev_code
        else:
            # Update the current code
            code = temp

        # Fill the buffer with all the needed codes
        while code >= 256:
            # Add the suffix code to our matched code buffer
            matched_code_buf.insert(0, prefix_suffix_map[code][1])
            # Get the prefix code
            code = prefix_suffix_map[code][0]

        # Add the last prefix code to our matched code buffer
        matched_code_buf.insert(0, code)
        # Update the last code
        last_code = code

        # Add new table entry
        if last_table_entry_index < bitmask:
            last_table_entry_index += 1
            prefix_suffix_map[last_table_entry_index] = (prev_code, last_code)

        # Update the previous code
        prev_code = temp

        # Add the matched code buffer to our decompressed output
        decompressed_output += matched_code_buf

    # Return the decompressed output as a `bytes` object
    return bytes(bytearray(decompressed_output))
