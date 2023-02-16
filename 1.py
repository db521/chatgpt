def regpt(pro):
    import openai
    openai.api_key = '你的key，替换一下'

    response = openai.Completion.create(
        model='text-davinci-003',
	    prompt=pro,
        temperature=1,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    answer=response.choices[0].text
    print(answer)
    return answer

if __name__ == '__main__':
    for x in range(10000):
        pro=input("请输入你的问题:")
        if pro=='继续':
            pro='Previous answer: '+regpt(pro)+' '
            regpt(pro)
        else:
            regpt(pro)%     
