import os
import json

class Choose_image:
    @staticmethod
    def the_last_image(image_folder: str, chosen_images_file=None):
        
            if not chosen_images_file:
                chosen_images_file = os.path.join(os.path.dirname(__file__), "chosen_images.json")

            if os.path.exists(chosen_images_file):
                with open(chosen_images_file, 'r', encoding='utf-8') as f:
                    chosen_images = json.load(f)
            else:
                chosen_images = []

            images = [f for f in os.listdir(image_folder) if f.endswith(('jpg', 'jpeg', 'png', 'gif','mp4',"mov","wmv"))]
            available_images = [image for image in images if image not in chosen_images]
            image_paths = [(os.path.join(image_folder, image), os.path.getctime(os.path.join(image_folder, image))) for image in available_images]
            sorted_images = sorted(image_paths, key=lambda x: x[1], reverse=False)
            oldest_image = sorted_images[0][0] if sorted_images else None

            if oldest_image:
                chosen_images.append(os.path.basename(oldest_image))
                with open(chosen_images_file, 'w', encoding='utf-8') as f:
                    json.dump(chosen_images, f, indent=2, ensure_ascii=False)
            return oldest_image
        
    @staticmethod
    def re_use_images(chosen_images_file = None):
        if not chosen_images_file:
            chosen_images_file = os.path.join(os.path.dirname(__file__), "chosen_images.json")
        with open(chosen_images_file, 'w', encoding='utf-8') as f:
                chosen_images = []
                json.dump(chosen_images, f, indent=2, ensure_ascii=False)

    

