import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_files(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='OZn0zZldGT0AAAAAAAAAAX_SWwPfRUJOu8imZIowHo-iE0ydGtX7wqn4Y_k2tgMx'
    transferdata=TransferData(access_token)
    file_from=input(" Enter The File You Wan't To Upload ")
    file_to=input(" Enter The Path You Want To Upload ")
    transferdata.upload_files(file_from,file_to)
    print("Your File Has Been Uploaded ")

main()

