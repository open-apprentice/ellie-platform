class Docsettings(object):
    title="Ellie Teaching and Learning Platform" 
    description = """
        We are teachers and so Ellie is neither complicated nor simplistic.
        Ellie is just right so you can focus on teaching and your students.
        Discover Ellie a modern teaching and learning platform. 
        """ 
    openapi_tags = [
        {
            "name": "index",
            "description": "The Web facing page with the **login screen**."
        },
        {
            "name": "create-user",
            "description": "**CREATE** new **Users** at /user."
        },
        {
            "name": "get-user",
            "description": "**GET** by *ID* a specific **User**.",
        },
        {
            "name": "delete-user",
            "description": "**DELETE** by *ID* a specific **User**.",
        },
            {
            "name": "create-course",
            "description": "**CREATE** a new **Course** at /course."
        },
        {
            "name": "get-course",
            "description": "**GET** a Course by *ID* a specific **Course**.",
        },
        {
            "name": "delete-course",
            "description": "**DELETE** a Course by *ID* a specific **Course**.",
        },
    ]
    version="0.0.1"
    terms_of_service="https://ellieplatform.org/terms-and-conditions/"
    contact={"name": "Ellie Platform", "url": "https://ellieplatform.org/contact"}
    license_info={"name": "MIT", "url": "https://github.com/open-apprentice/ellie/blob/main/LICENSE", }
    
docsettings = Docsettings()