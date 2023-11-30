from .models import PersonalDocument, TruckDocument, CargoDocument


def get_all_documents():
    all_documents = []
    personal_documents = PersonalDocument.objects.all()
    all_documents.extend(personal_documents)
    truck_documents = TruckDocument.objects.all()
    all_documents.extend(truck_documents)
    cargo_documents = CargoDocument.objects.all()
    all_documents.extend(cargo_documents)

    print(all_documents)
    return all_documents