from PIL import Image
import os
import random

def show_reference_image(category, gender=None, flip=False):
    image_folder = "/Users/nataliehuang/Desktop/PFDA/DrawingReferences/images"

    image_mapping = {
        "human": {
            "male": ["male_reference.jpeg", "MaleSuit_Reference.jpeg"],
            "female": ["Female_Reference.jpeg", "FemaleDress_Reference.jpeg"]
        },
        "animal": ["Cat_Reference.jpeg", "Cow_Reference.jpeg", "Deer_Reference.jpeg", "Dog_Reference.jpeg", "Snake_Reference.jpeg"],
        "object": ["Cheese Reference.jpeg", "Cup_Reference.jpeg", "Die_Reference.jpeg", "Flower_Reference.jpeg", "King_Reference.jpeg", "Knife_Reference.jpeg", "Pear_Reference.jpeg", "Pie_Reference.jpeg"],
        "place": ["China_Reference.jpeg", "CommunistApartment_Reference.jpeg", "Desert_Reference.jpeg", "HouseFire_Reference.jpeg", "LOTR_Reference.jpeg", "Paris_Reference.jpeg", "Restraunt_Reference.jpeg", "Romania_Reference.jpeg"]
    }

    # Check if the specified category exists in the mapping
    if category in image_mapping:
        if isinstance(image_mapping[category], dict):
            if gender is None:
                # If no specific gender is provided, choose a random one
                gender = random.choice(list(image_mapping[category].keys()))
            
            # Check if the specified gender exists in the mapping
            if gender in image_mapping[category]:
                image_filenames = image_mapping[category][gender]
            else:
                print(f"No reference image available for gender: {gender} in the {category} category")
                return
        else:
            image_filenames = image_mapping[category]

        # Choose a random image filename for the specified category and gender
        image_filename = random.choice(image_filenames)
        image_path = os.path.join(image_folder, image_filename)

        # Check if the image file exists
        if os.path.exists(image_path):
            reference_image = Image.open(image_path)

            # Flip the image horizontally if requested
            if flip:
                reference_image = reference_image.transpose(Image.FLIP_LEFT_RIGHT)

            reference_image.show()
        else:
            print(f"No reference image found for {category}, {gender}, and {image_filename}")
    else:
        print(f"No reference image available for category: {category}")

def main():
    # Ask the user for input
    user_input_category = input("What do you need a reference for? human, animal, object, or place? ")

    # If the category is "human," ask for gender
    if user_input_category.lower() == "human":
        user_input_gender = input("Enter gender (male/female), or press Enter for a random gender: ")
    else:
        user_input_gender = None

    # Ask the user if they want to flip the image horizontally
    flip_image = input("Do you want to flip the image horizontally? (yes/no): ").lower() == 'yes'

    # Show the reference image based on the user's input
    show_reference_image(user_input_category, user_input_gender, flip_image)

if __name__ == "__main__":
    main()
