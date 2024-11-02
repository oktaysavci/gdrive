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
    
    file_id = file.get('id')
    print(f"Dosya başarıyla yüklendi. Dosya ID'si: {file_id}")
    
    # Dosyaya herkese açık erişim izni ekle
    permission = {
        'type': 'anyone',  # Dosyayı herkese açar
        'role': 'reader'   # Yalnızca okuma izni verir
    }
    
    service.permissions().create(
        fileId=file_id,
        body=permission
    ).execute()
    
    print("Dosya herkese açık hale getirildi.")

# Kullanıcıdan dosya yolunu ve adını iste
file_path = input("Lütfen yüklenecek dosyanın yolunu girin: ")
file_name = input("Google Drive'da görünecek dosya adını girin: ")

# Dosyayı yükle
upload_to_drive(file_path, file_name)
