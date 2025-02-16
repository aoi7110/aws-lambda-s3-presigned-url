import requests
import json

def get_presigned_url(api_url, file_name):
    """
    API から presigned URL を取得する関数
    """
    payload = {"file_name": file_name}
    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
    data = response.json()
    
    # 返却される JSON の形式が {"upload_url": "..." } の場合
    presigned_url = data.get("upload_url")
    if not presigned_url:
        raise ValueError("Presigned URL not found in API response.")
    return presigned_url

def upload_image(upload_url, image_path):
    """
    presigned URL を利用して画像を S3 にアップロードする関数
    """
    headers = {"Content-Type": "image/jpeg"}
    with open(image_path, "rb") as f:
        image_data = f.read()
    
    # PUT リクエストで画像データを送信。allow_redirects=True でリダイレクトにも対応
    response = requests.put(upload_url, data=image_data, headers=headers, allow_redirects=True)
    return response

if __name__ == "__main__":
    # presigned URL を取得する API のエンドポイント
    api_url = "https://ocgmxbtnn1.execute-api.ap-southeast-2.amazonaws.com/mystage/20250211_generate-presigned-url"
    # S3 に保存するファイル名（API に渡すパラメータ）
    file_name = "test-image.jpg"
    # アップロードするローカルの画像ファイルのパス
    image_path = r"C:\Users\aoi71\test-image.jpg"
    
    try:
        # presigned URL を取得
        presigned_url = get_presigned_url(api_url, file_name)
        print("Presigned URL obtained:")
        print(presigned_url)
        
        # 画像をアップロード
        response = upload_image(presigned_url, image_path)
        if response.status_code in [200, 204]:
            print("Image upload succeeded!")
        else:
            print("Image upload failed. Status code:", response.status_code)
            print("Response text:", response.text)
    except Exception as e:
        print("An error occurred:", e)
