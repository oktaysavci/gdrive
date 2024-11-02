from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_to_drive(file_path, file_name):
    # Google Drive API kimlik bilgileri
    creds = service_account.Credentials.from_service_account_file('api.json')
    service = build('drive', 'v3', credentials=creds)
    
    # Yüklenecek dosya için medya ayarlaması
    media = MediaFileUpload(file_path, resumable=True)
    
    # Dosya meta verileri
    file_metadata = {
        'name': file_name,
        'mimeType': 'application/octet-stream'
    }
    
    # Dosyayı yükle
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    
    print(f"Dosya başarıyla yüklendi. Dosya ID'si: {file.get('id')}")

file_path = input("Lütfen yüklenecek dosyanın yolunu girin: ")
file_name = input("Google Drive'da görünecek dosya adını girin: ")

# Dosyayı yükle
upload_to_drive(file_path, file_name)

