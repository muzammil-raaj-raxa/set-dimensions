from PIL import Image
import os

def create_images_with_user_images(input_folder, output_folder, background_width, background_height):
    try:
        os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist

        input_image_paths = [os.path.join(input_folder, filename) for filename in os.listdir(input_folder) if filename.lower().endswith(('.jpg', '.jpeg', '.png'))]

        for i, input_image_path in enumerate(input_image_paths):
            # Create a new white background image with transparency (RGBA)
            background = Image.new("RGBA", (background_width, background_height), (255, 255, 255, 0))

            # Open the user-uploaded image
            user_image = Image.open(input_image_path).convert("RGBA")

            # Calculate the scaling factor to fit the user image within the background
            width_ratio = background_width / user_image.width
            height_ratio = background_height / user_image.height

            # Use the minimum scaling factor to ensure the entire image fits within the background
            min_ratio = min(width_ratio, height_ratio)

            # Resize the user image to fit within the background dimensions
            new_width = int(user_image.width * min_ratio)
            new_height = int(user_image.height * min_ratio)
            user_image = user_image.resize((new_width, new_height))

            # Calculate the position to center the user image within the background
            x = (background_width - new_width) // 2
            y = (background_height - new_height) // 2  # Center vertically

            # Paste the user image onto the background
            background.paste(user_image, (x, y), user_image)

            # Generate the output image path with the same filename in the output folder
            output_image_path = os.path.join(output_folder, os.path.basename(input_image_path))

            # Save the final image as a PNG with transparency
            background.save(output_image_path, format="PNG")

            print(f"Image {i + 1} created with user image centered and saved to {output_image_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_folder = "./input"  # Input folder containing all the images
    output_folder = "./final"  # Output folder for the generated images
    background_width = 700
    background_height = 300

    create_images_with_user_images(input_folder, output_folder, background_width, background_height)


