 ################################################################################
#   Author:         Justin Berthelot                                            #
#   Date:           02/17/2025                                                  #
#   Description:    LZW compression and decompression in "pure" python          #
#                   alongside mirroring of UNIX compress/uncompress             #
#                   functionality.                                              #
################################################################################

from argparse import ArgumentParser
from os import name, path, remove
from sys import stdout
from pyunixlzw import compress
from pyunixlzw import decompress

# OS check
if name == 'nt':
    # The stupid way
    FILE_DELIM = '\\'
else:
    # The right way
    FILE_DELIM = '/'

def handle_compress(filename, maxbits):
    """Compresses data within a given file.
    
    Parameters:
    - `str` filename
        - The file to be compressed
    - `int` maxbits
        - The maximum bit length available for entries in the code table
    
    Return:
    - `tuple[bytes, bytes]` | `None`
        - The compressed output stream
        - The decompressed output stream
    """
    # Open the file
    try:
        with open(filename, 'rb') as f:
            decompressed_data = f.read()
    except FileNotFoundError:
        print(f"{filename}: No such file or directory")
        exit()
    except PermissionError:
        print(f"{filename}: Permission denied")
        exit()
    except Exception as e:
        print(f"{filename}: Could not open file for reading")
        exit()
    
    # Compress the data
    compressed_data = compress(
        decompressed_data=decompressed_data,
        max_bit_len=maxbits
    )

    # Return the compressed and decompressed data
    return (compressed_data, decompressed_data)

def handle_decompress(filename, maxbits):
    """Decompresses data within a given file.
    
    Parameters:
    - `str` filename
        - The file to be decompressed
    - `int` maxbits
        - The maximum bit length available for entries in the code table
    
    Return:
    - `tuple[bytes, bytes]` | `None`
        - The compressed output stream
        - The decompressed output stream
    """
    # Open the file
    try:
        with open(filename, 'rb') as f:
            compressed_data = f.read()
    except FileNotFoundError:
        print(f"{filename}: No such file or directory")
        exit()
    except PermissionError:
        print(f"{filename}: Permission denied")
        exit()
    except Exception as e:
        print(f"{filename}: Could not open file for reading")
        exit()
    
    # Decompress the data
    decompressed_data = decompress(
        compressed_data=compressed_data,
        max_bit_len=maxbits
    )

    # Return the compressed and decompressed data
    return (compressed_data, decompressed_data)

def handle_file_overwrite(output_path, output_filename):
    """Handles the functionality to check whether we need to overwrite a file.
    
    Parameters:
    - `str` output_path
        - The path to the file we want to write to
    - `str` output_filename
        - The name of the output file
    
    Return:
    - `bool`
        - Determination on whether we can write to the file
    """
    # Check if we are overwriting a file
    if path.exists(output_path):
        # Let the user know
        print(f"{output_filename} already exists.")
        # User input to continue
        resp = input(f"Do you wish to overwrite {output_filename} (y/N)? ")
        # Halt processing
        if len(resp) == 0 or resp[0].lower() == 'n':
            return False
    # Continue as planned
    return True

def handle_output_to_file(output_path, output_filename, output_data):
    """Handles the functionality to output data to a file and print results to the console.
    
    Parameters:
    - `str` output_path
        - The path to the file we want to write to
    - `str` output_filename
        - The name of the output file
    - `bytes` output_data
        - The data that we want to write
    
    Return:
    - `bool`
        - Successful file write
    """
    
    # Open and write
    try:
        with open(output_path, 'wb') as f:
            f.write(output_data)
        # Success
        return True
    except PermissionError:
        print(f"{output_filename}: Permission denied")
    except Exception as e:
        print(f"{output_filename}: Could not open file for writing")
    # Failure
    return False

def handle_remove_file(input_path, input_filename):
    """Handles the functionality to remove the original input file.
    
    Parameters:
    - `str` input_path
        - The path to the file we want to remove
    - `str` input_filename
        - The name of the original input file that we want to remove
    
    Return:
    - `bool`
        - Successful file removal
    """
    # Try to remove the old file
    try:
        remove(input_path)
        # Success
        return True
    except PermissionError:
        print(f"rm: cannot remove '{input_filename}': Operation not permitted")
    except Exception as e:
        print(f"pyunixlzw: Could not remove '{input_filename}': {e}")
    # Failure
    return False

def get_compression_ratio(compressed_data, decompressed_data):
    """Returns the compression ratio as a string.
    
    Parameters:
    - `bytes` compressed_data
        - The compressed data that we processed
    - `bytes` decompressed_data
        - The decompressed data that we processed
    
    Return:
    - `str`
        - The compression ratio 
    """
    # Quick statistics calculation 
    return f" Compression: {round(1 - (len(compressed_data) / len(decompressed_data)), 2)}%"

def handle_version():
    """Returns the version and author information."""
    return "pyunixlzw version: 1.0.0.0\n\nAuthor: Justin Berthelot"

def main():
    # Standard argparse
    parser = ArgumentParser(
        prog='pyunixlzw',
        description='A pure-Python3 implementation of UNIX compress and decompress.'
    )

    # Filename
    parser.add_argument('file')

    # Decompress
    parser.add_argument('-d', '--decompress',
        action="store_true",
        help="If given, decompression is done instead."
    )

    # stdout
    parser.add_argument('-c', '--stdout',
        action="store_true",
        help="Write output on stdout, don't remove original."
    )

    # Maximum Bit Length
    parser.add_argument('-b', '--maxbits',
        help="Parameter limits the max number of bits/code.",
        type=int
    )

    # Force Output File
    parser.add_argument('-f', '--force',
        action="store_true",
        help="Forces output file to be generated, even if one already " +
            "exists, and even if no space is saved by compressing. "
    )

    # Compresssion Statistics
    parser.add_argument('-v', '--stats',
        action="store_true",
        help="Write compression statistics."
    )
    
    # Version
    parser.add_argument('-V', '--version',
        action="store_true",
        help="Output version and author."
    )

    # Parse arguments
    args = parser.parse_args()

    # Version
    if args.version:
        handle_version()
        exit()
    
    # Max bits are needed for compress / decompress
    if args.maxbits is not None:
        maxbits = args.maxbits
    else:
        # Default to 16
        maxbits = 16

    # Decompress / compress
    if args.decompress:
        compressed_data, decompressed_data = handle_decompress(args.file, maxbits)
        output_path = args.file[:-2] if args.file[-2:] == '.Z' else args.file
        output_data = decompressed_data
    # If -d was not specified, we are compressing
    else:
        compressed_data, decompressed_data = handle_compress(args.file, maxbits)
        output_path = args.file + '.Z'
        output_data = compressed_data
    
    # Write to stdout
    if args.stdout:
        stdout.write(output_data)
        return
    # Write to file
    else:
        # Get the filename for the original input file
        input_filename = args.file.split(FILE_DELIM)[-1]
        # Get the filename for the output file
        output_filename = output_path.split(FILE_DELIM)[-1]

        # Determine whether we can continue or not
        if args.force is None and not handle_file_overwrite(output_path, output_filename):
            print(f"{output_filename} not overwritten")
            return

        # Try to output to new file
        if not handle_output_to_file(output_path, output_filename, output_data):
            return

        # Try to remove old input file
        if not handle_remove_file(args.file, input_filename):
            return
        
        # Get the compression ratio if the user asked for it
        if args.stats:
            pct = get_compression_ratio(compressed_data, decompressed_data)
        else:
            pct = ''
        
        # Output the final result
        print(f"{input_filename}:  -- replaced with {output_filename}" + pct)

if __name__ == '__main__':
    main()