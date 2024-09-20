from pymongo import MongoClient
from pymongo.errors import PyMongoError, ConnectionFailure

# Підключення до MongoDB
try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["animals"]
    # Перевірка з'єднання
    client.admin.command('ismaster')
    print("MongoDB підключено успішно")
except ConnectionFailure:
    print("Не вдалося підключитися до MongoDB, перевірте з'єднання")


def create_document():
    try:
        name = input("Введіть ім'я тварини")
        age = int(input("Введіть вік тварини"))
        features_input = input("Введіть особливості тварини, розділені комою")
        features = features_input.split(", ")
        document={"name":name, "age":age, "features":features}
        collection.insert_one(document)
        print("Документ створено.")
    except PyMongoError as e:
        print(f"Помилка при роботі з MongoDB: {e}")
    except ValueError as e:
        print(f"Помилка введення: {e}")


def read_all_documents():
 documents= list(collection.find({}))
 for doc in documents:
  print(doc)

def read_document_by_name():
 name = input("Введіть ім'я тварини")
 res = collection.find_one({"name":name})
 print(res)


def update_document_age():

    name = input("Введіть ім'я тварини")
    collection.find_one({"name":name})
    age = input("Введіть вік тварини")
    res=collection.update_one({"name": name}, {"$set": {"age": age}})
    print("Вік оновлено")


def add_feature_to_document():
   name = input("Введіть ім'я тварини")
   collection.find_one({"name":name})
   features= input("Введіть особливості тварини, розділені комою")
   res=collection.update_one({"name": name},{"$push": {"features" : features}})
   print(res,"Особливість додано")

def delete_document():

    name = input("Введіть ім'я тварини")
    collection.find_one({"name":name})
    x=collection.delete_one({"name":name})
    return x.deleted_count,"Документ видалено")

def delete_all_documents():
    x=collection.delete_many({})
    
    return x.deleted_count,"Всі документи видалено"


def main():
    while True:
        print("\nДоступні дії:")
        print("1 - Створити запис про тварину")
        print("2 - Показати всі записи")
        print("3 - Пошук запису за ім'ям тварини")
        print("4 - Оновити вік тварини")
        print("5 - Додати особливість до тварини")
        print("6 - Видалити запис про тварину")
        print("7 - Видалити всі записи")
        print("8 - Вийти")
        choice = input("Виберіть дію: ")

        if choice == "1":
            create_document()
        elif choice == "2":
            read_all_documents()
        elif choice == "3":
            read_document_by_name()
        elif choice == "4":
            update_document_age()
        elif choice == "5":
            add_feature_to_document()
        elif choice == "6":
            delete_document()
        elif choice == "7":
            delete_all_documents()
        elif choice == "8":
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()