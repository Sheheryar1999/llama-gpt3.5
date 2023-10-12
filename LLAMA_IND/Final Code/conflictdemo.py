from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.1")

def get_conflicts():
    db = client.contextdb
    collection = db.chat_responses
    collections = []
    for document in collection.find({"label": {"$ne": ""}, "role": "assistant"}):
        collections.append(document)

    return collections

def update_conflicts(collection_id, new_contents, new_label):
    db = client.contextdb
    collection = db.chat_responses
    result = collection.update_one(
        {"_id": collection_id},
        {"$set": {"content": new_contents, "label": new_label}}
    )

    return result.modified_count

def get_label():
    collections = get_conflicts()
    collections_by_label = {}

    for document in collections:
        label = document["label"]
        if label not in collections_by_label:
            collections_by_label[label] = []
        collections_by_label[label].append(document)

    for label, collections in collections_by_label.items():
        print(f"Label: {label}")
        for collection in collections:
            print(collection)
            print("\n")

def get_user_input():
    new_contents = input("Enter corrected content: ")
    new_label = input("Enter new label: ")
    return new_contents, new_label

def main():
    collections = get_conflicts()

    # Print available labels
    print("Available labels:")
    for idx, collection in enumerate(collections):
        print(f"{idx + 1}. {collection['label']}")

    choice = int(input("Enter the number of the label you want to update: "))
    chosen_collection = collections[choice - 1]

    new_contents, new_label = get_user_input()

    update_result = update_conflicts(
        chosen_collection["_id"],
        new_contents,
        new_label
    )

    if update_result > 0:
        print(f"Collection updated successfully.")
        print(f"New contents: {new_contents}")
        print(f"New label: {new_label}")
    else:
        print(f"Failed")

if __name__ == "__main__":
    main()
