from PIL import Image
import os
import random

def show_reference_image(category, gender=None):
    image_folder = "/Users/nataliehuang/Desktop/PFDA/DrawingReferences/images"

    # Define a mapping between categories, gender, and image filenames
    image_mapping = {
        "human": {
            "male":["male_reference.jpeg", "MaleSuit_Reference.jpeg"]
            "female": ["Female_Reference.jpeg", "FemaleDress_Reference.jpeg"]
        },
        "animal": ["Cat_Reference.jpeg", "Cow_Reference.jpeg"],
        "object": ["Cheese Reference.jpeg", "Cup_Reference.jpeg"],
        "place": ["China_Reference.jpeg", "CommunistApartment_Reference.jpeg"]
    }

    # Check if the specified category exists in the mapping
    if category in image_mapping:
        if gender is None:
            # If no specific gender is provided, choose a random one (if applicable)
            if isinstance(image_mapping[category], dict):
                gender = random.choice(["male", "female"])

        # Check if the specified gender exists in the mapping
        if gender in image_mapping[category]:
            image_filename = image_mapping[category][gender]
            image_path = os.path.join(image_folder, image_filename)

            # Check if the image file exists
            if os.path.exists(image_path):
                reference_image = Image.open(image_path)
                reference_image.show()
            else:
                print(f"No reference image found for {category} and {gender}")
        else:
            print(f"No reference image available for gender: {gender} in the {category} category")
    else:
        print(f"No reference image available for category: {category}")

def main():
    # Ask the user for input
    user_input_category = input("What do you need a reference for? Enter a specific category: ")

    # If the category is "human," randomly choose a gender
    if user_input_category.lower() == "human":
        show_reference_image(user_input_category)
    else:
        show_reference_image(user_input_category)

if __name__ == "__main__":
    main()
