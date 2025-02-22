import pandas as pd
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from .model_utils import get_label_mappings

def train_text_classifier(labels, train_file, test_file, model_name, output_dir):
    """
    Train a text classifier using the user-defined labels.

    Args:
    - labels (list): List of user-defined labels.
    - train_file (str): Path to the training CSV file.
    - test_file (str): Path to the test CSV file.
    - model_name (str): Pretrained model name.
    - output_dir (str): Directory to save trained model.
    """
    # Convert label names to numerical IDs
    label2id, id2label = get_label_mappings(labels)

    # Load CSV data
    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)

    # Convert text labels to numerical IDs
    train_df["label"] = train_df["label"].map(label2id)
    test_df["label"] = test_df["label"].map(label2id)

    # Save preprocessed CSVs (optional for debugging)
    train_df.to_csv("train_numeric.csv", index=False)
    test_df.to_csv("test_numeric.csv", index=False)

    # Load dataset into Hugging Face format
    dataset = load_dataset("csv", data_files={"train": "train_numeric.csv", "test": "test_numeric.csv"})

    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(
        model_name, num_labels=len(labels), ignore_mismatched_sizes=True
    )

    # Apply tokenization
    def preprocess(example):
        return tokenizer(example["text"], truncation=True, padding="max_length")

    dataset = dataset.map(preprocess, batched=True)

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        num_train_epochs=3,
        weight_decay=0.01,
        push_to_hub=False,
    )

    # Train the model
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"]
    )

    trainer.train()

    # Save model and tokenizer
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
