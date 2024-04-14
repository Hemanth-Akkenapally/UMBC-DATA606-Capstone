import os

def list_image_paths(directory, extension='.jpg'):
    image_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                image_paths.append(os.path.join(root, file))
    return image_paths

def write_paths_to_file(image_paths, output_file):
    with open(output_file, 'w') as f:
        for path in image_paths:
            f.write(path + '\n')

if __name__ == "__main__":
    
    input_directory = input("Enter the input directory path: ")
    
    
    output_file = input("Enter the output file name: ")
    
    
    image_paths = list_image_paths(input_directory)
    
    
    write_paths_to_file(image_paths, output_file)
    
    print(f"Image paths are saved to {output_file}")
