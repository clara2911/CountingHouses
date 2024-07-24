from transformers import (
    Trainer,
    AutoImageProcessor,
    AutoModelForObjectDetection,
    TrainingArguments
)
from house_detector import HouseDetector
from datasets import load_dataset
from PIL import ImageDraw
import albumentations
import numpy as np


class DETRHouseDetector(HouseDetector):
    def __init__(self):
        self.checkpoint = "facebook/detr-resnet-50"
        self.image_processor = None
        self.model = None
        self.dataset_id2label = None
        self.dataset_label2id = None
        self.cppe5 = None
        self.transform = None

    def load_train_dataset(self):
        self.cppe5 = load_dataset("cppe-5")
        image = self.cppe5["train"][0]["image"]
        annotations = self.cppe5["train"][0]["objects"]
        draw = ImageDraw.Draw(image)

        categories = self.cppe5["train"].features["objects"].feature["category"].names
        self.dataset_id2label = {index: x for index, x in enumerate(categories, start=0)}
        self.dataset_label2id = {v: k for k, v in self.dataset_id2label.items()}
        for i in range(len(annotations["id"])):
            box = annotations["bbox"][i - 1]
            class_idx = annotations["category"][i - 1]
            x, y, w, h = tuple(box)
            draw.rectangle((x, y, x + w, y + h), outline="red", width=1)
            draw.text((x, y), self.dataset_id2label[class_idx], fill="white")

        remove_idx = [590, 821, 822, 875, 876, 878, 879]
        keep = [i for i in range(len(self.cppe5["train"])) if i not in remove_idx]
        self.cppe5["train"] = self.cppe5["train"].select(keep)

    def load_image_processor(self):
        self.image_processor = AutoImageProcessor.from_pretrained(self.checkpoint)


    def preprocess_finetune_dataset(self):
        self.transform = albumentations.Compose(
            [
                albumentations.Resize(480, 480),
                albumentations.HorizontalFlip(p=1.0),
                albumentations.RandomBrightnessContrast(p=1.0),
            ],
            bbox_params=albumentations.BboxParams(format="coco", label_fields=["category"]),
        )
        self.cppe5["train"] = self.cppe5["train"].with_transform(self.transform_aug_ann)
        self.cppe5["train"][15]

    def formatted_annotations(self, image_id, category, area, bbox):
        annotations = []
        for i in range(0, len(category)):
            new_ann = {
                "image_id": image_id,
                "category_id": category[i],
                "isCrowd": 0,
                "area": area[i],
                "bbox": list(bbox[i]),
            }
            annotations.append(new_ann)

        return annotations

    def transform_aug_ann(self, examples):
        image_ids = examples["image_id"]
        images, bboxes, area, categories = [], [], [], []
        for image, objects in zip(examples["image"], examples["objects"]):
            image = np.array(image.convert("RGB"))[:, :, ::-1]
            out = self.transform(image=image, bboxes=objects["bbox"], category=objects["category"])

            area.append(objects["area"])
            images.append(out["image"])
            bboxes.append(out["bboxes"])
            categories.append(out["category"])

        targets = [
            {"image_id": id_, "annotations": self.formatted_annotations(id_, cat_, ar_, box_)}
            for id_, cat_, ar_, box_ in zip(image_ids, categories, area, bboxes)
        ]

        return self.image_processor(images=images, annotations=targets, return_tensors="pt")

    def load_model(self):
        self.model = AutoModelForObjectDetection.from_pretrained(
            self.checkpoint,
            id2label=self.dataset_id2label,
            label2id=self.dataset_label2id,
            ignore_mismatched_sizes=True,
        )

    def finetune_model(self):
        training_args = TrainingArguments(
            output_dir="detr-resnet-50_finetuned_cppe5",
            per_device_train_batch_size=8,
            num_train_epochs=10,
            fp16=True,
            save_steps=200,
            logging_steps=50,
            learning_rate=1e-5,
            weight_decay=1e-4,
            save_total_limit=2,
            remove_unused_columns=False,
            push_to_hub=True,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            data_collator=self.collate_fn,
            train_dataset=self.cppe5["train"],
            tokenizer=self.image_processor,
        )
        trainer.train()
        trainer.push_to_hub()

    def collate_fn(self, batch):
        pixel_values = [item["pixel_values"] for item in batch]
        encoding = self.image_processor.pad(pixel_values, return_tensors="pt")
        labels = [item["labels"] for item in batch]
        batch = {"pixel_values": encoding["pixel_values"], "pixel_mask": encoding["pixel_mask"], "labels": labels}
        return batch

    def detect_houses(self, model, image_path):
        pass


if __name__ == "__main__":
    detector = DETRHouseDetector()
    detector.load_train_dataset()
    detector.load_image_processor()
    detector.preprocess_finetune_dataset()
    detector.load_model()
    detector.finetune_model()
