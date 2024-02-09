import argparse
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer

def interact_with_model(model, tokenizer):
    while True:
        user_input = input("Enter a prompt (type 'exit' to end): ")
        if user_input.lower() == 'exit':
            break

        input_ids = tokenizer.encode(user_input, return_tensors='pt', max_length=512)
        output_ids = model.generate(input_ids)

        generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        print("Generated Text:", generated_text)

def main():

    parser = argparse.ArgumentParser(description="Interact with a T5 model")
    parser.add_argument("--model_path", type=str, required=True, help="Path to the trained T5 model")

    args = parser.parse_args()
    model_path = args.model_path  # Replace with the actual path
    model = T5ForConditionalGeneration.from_pretrained(model_path)
    tokenizer = T5Tokenizer.from_pretrained("Salesforce/codet5-base")

    model.eval()
    interact_with_model(model, tokenizer)

if __name__ == "__main__":
    main()
