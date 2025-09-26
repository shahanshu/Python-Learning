import random



class fakellm:
    def __init__(self):
        print(" LLm created")

    def predict(self,prompt):
        response_list=[
            'this is me',
            'This is you but not me ',
            'this can be you or be',
            
            'Either of us is you'
        ]

        return({

           'response':random.choice(response_list)
        }
        )


class faketemplate:
    def __init__(self,template,input_variables):
        self.template= template
        self.intput_variables= input_variables


    def format(self,input_dict):
        return self.template.format(**input_dict)



template=faketemplate(
    template="write a poem about {topic}",
    input_variables=['topic']
)

prompt  =template.format(
    {
        'topic':'nepal'
    }
)

llm=fakellm()
result=llm.predict(prompt)
print(result)
# llm = fakellm()
# result =llm.predict('what is the capital of nepal')
# print(result)