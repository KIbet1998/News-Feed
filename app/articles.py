class Articles:
    '''
    Class that define news objects
    '''
    def __init__(self,id,author,title,description,url,image,date):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url= url
        self.image = image
        self.date = date