# ConvSearch Dataset
This repository is the home of the  **C**hinese **O**pen-Domai**n** Con**v**ersational **Search** Behavior Dataset (ConvSearch). You can refer to paper [ConvSearch: A Open-Domain Conversational Search Behavior Dataset](https://arxiv.org/pdf/2204.02659.pdf) for more details on dataset construction and analysis.



## Download data

Our dataset contains the following parts:

- Dialogues (Main part, **Dialogs.json**): information of dialogue and corresponding turns, including content, timestamp, annotation results, et al.
- Agent behaviors (Main part, **SearchBehaviors.json**): the information seeking behaviors of agent before they respond to users, including query requests, SERPs with click action, landing pages.
- The HTML files of SERPs (search engine result pages, **SERP-htmls.tar.gz**) and landing pages in agent search behavior (Supplementary part, **Landing-page-htmls.tar.gz**).
- Image files in dialogues (Supplementary part, **Dialog-images.tar.gz**).



Following table shows the download links of ConvSearch dataset:

| Version | Release time | Main part | Full data |
| ------- | --------- | --------- | --------- |
| 1.1 | 2022/02/28 | [ConvSearch-v1.1-Main.zip](https://drive.google.com/file/d/1Bhgwrm12Msx9XBs--9zpCXxJ4n-MM1QJ/view?usp=sharing) (4.3MB) | [ConvSearch-v1.1-Full.zip](https://drive.google.com/file/d/1YUEXF67UBHDWOvHqRNhZfU0Q4mRQKX45/view?usp=sharing) (1.5GB) |



## Dialogs.json Format

**Dialogs.json** is provided as json format with an array of dialogues. For each dialogue, following show its segments as well as their corresponding descriptions.

- id: the dialogue id
- user: the id of the dialogue-participated user
- agent: the id of the dialogue-participated agent
- start_time: the timestamp of the dialogue start timestamp
- end_time: the timestamp of the dialogue end timestamp
- topic_user: the user-annotated dialogue topic
- effort_user: the user-annotated dialogue-level effort
- preference_user: the user's preference between conversational search and traditional query-SERP search with the information need of this dialogue
- applicability_user: the degree to which the user apply the information or suggestions provided by the agent after dialogue
- improvement_user: the user's improvement suggestions towards agent responses
- understand_agent: the degree to which the agent understand user’s information need of the whole dialogue from the agent perspective
- satisfaction_agent: the degree of agent-perceived user’s satisfaction towards agent responses of the entire conversation
- difficulty_agent: the difficulty for the agent to meet user’s information need in the whole dialogue
- keywords: the user provided keywords of the dialogue before the dialogue starts
- turns: an array containing the information of each turn, sorted with the turn timestamp
  - id: the turn id
  - content: the content of the turn (image type turn is empty string)
  - initiator: the role that initiates this turn of dialogue (user or agent)
  - time: the timestamp when this turn is generated
  - is_image: whether this turn is in image type
  - image_name: the image file name if this turn is in image type
  - satisfaction-turn: the degree to which the user feel satisfied with the agent response in the current turn (only for agent-initiated turn)
  - understand-turn: the degree to which the user feels that the agent has understood his or her search intent  (only for agent-initiated turn)
  - action-primary-class: the primary labels (an array of labels for each assessor) for agent action annotation (only for agent-initiated turn)
  - action-secondary-class: the secondary labels (an array of labels for each assessor) for agent action annotation (only for agent-initiated turn)
  - clarity-turn: the degree of clarity in expression of user information need in the current turn (only for user-initiated turn)
  - difficulty-turn: the difficulty of satisfying user’s information need in the current turn (only for user-initiated turn)
  - intent-primary-class: the primary labels (an array of labels for each assessor) for user intent annotation (only for user-initiated turn)
  - intent-secondary-class: the secondary labels (an array of labels for each assessor) for user intent annotation (only for user-initiated turn)



### Sample of Dialogs.json 

Following show the sample content of Dialogs.json:

```json
[{
  "id": 130, 
  "user": 14, 
  "agent": 13, 
  "start_time": 1637848232.193, 
  "end_time": 1637849330.969, 
  "topic_user": "food", 
  "intent_user": "\u5bfb\u627e\u597d\u5403\u7684\u6c49\u5821", 
  "satisfaction_user": 4, 
  "effort_user": 3, 
  "preference_user": 0, 
  "applicability_user": 3, 
  "improvement_user": "\u662f\u5426\u53ef\u4ee5\u7ed9\u51fa\u4e00\u4e9b\u5546\u54c1\u7684\u8bc4\u5206\u6216\u8005\u8bc4\u4ef7\u4fe1\u606f\uff0c\u65b9\u4fbf\u4f9d\u636e\u5bf9\u6bd4", 
  "understand_agent": 4, 
  "satisfaction_agent": 4, 
  "difficulty_agent": 2, 
  "keywords": "\u7f8e\u98df", 
  "turns": [
    {
      "id": 1093, 
     "content": "\u80af\u5fb7\u57fa\u548c\u9ea6\u5f53\u52b3\u7684\u6c49\u5821\u54ea\u5bb6 \uff1f", 
     "initiator": "user", 
     "time": 1637848232.193, 
     "is_image": false, 
     "image_name": "", 
     "clarity-turn": 3, 
     "difficulty-turn": 2, 
     "intent-primary-class": ["reveal-initiate", "reveal-initiate", "reveal-initiate"], 
     "intent-secondary-class": ["", "", ""]
    }, 
    {
      "id": 1094, 
     "content": "\u8bf7\u95ee\u4f60\u60f3\u95ee\u7684\u662f\u80af\u5fb7\u57fa\u548c\u9ea6\u5f53\u52b3\u6709\u4ec0\u4e48\u6c49\u5821\u5417\uff1f", 
     "initiator": "agent", 
     "time": 1637848282.757, 
     "is_image": false, 
     "image_name": "", 
     "satisfaction-turn": 4, 
     "understand-turn": 4, 
     "action-primary-class": ["clarify", "clarify", "clarify"], 
     "action-secondary-class": ["", "", ""]} ......
```

As a Chinese conversational search dataset, we have stored the conversational content using Unicode encoding to ensure that users can successfully decode the data in any environment. You can refer to the *annotation-rules* folder to see the annotation specifications for the corresponding segments.



## SearchBehaviors.json Format

**SearchBehaviors.json** is provided as json format with an array of query requests. For each query request, following show its segments as well as their corresponding descriptions.

- id: the query request id
- query_string: the query content agent submits to the search engine
- origin: the agent-selected Chinese search engine or knowledge acquisition platform (one of baidu, sogou, bing, zhihu and douban)
- time: the timestamp when the query request is generated
- belong_dialog: the id for the associated dialogue
- belong_turn: the id for the associated dialogue turn
- serp_pagelogs: an array containing the information of each agent-browsed Search Engine Result Page (SERP), sorted with the start timestamp
  - id: the SERP log id
  - url: the URL of this SERP
  - html_name: the stored SERP HTML filename
  - start_time: the timestamp when agent opens this SERP
  - end_time: the timestamp when agent closes this SERP
  - dwell_time: the duration agent dwells on this SERP (unit: millisecond)
  - page_id: the page num of the SERP in the search engine (for example page_id 1 for the top-10 results, page_id 2 for the rank 11~20 results)
  - clicked_results: an array containing the information of each clicked result pages
    - href: the clicked result URL
    - type: the clicked result type (content: general landing page, tab: the link of navigator tab)
    - id: the rank of this clicked result (sorted with the display order)
- landingpage_pagelogs: an array containing the information of each agent-browsed landing pages, sorted with the start timestamp
  - id: the landing page log id
  - helpfulness-pagelog: the degree to which this webpage is helpful in generating agent response
  - url: the URL of this landing page
  - html_name: the stored landing page HTML filename
  - start_time: the timestamp when agent opens this landing page
  - end_time: the timestamp when agent closes this landing page
  - dwell_time:  the duration agent dwells on the this SERP (unit: millisecond)



### Sample of SearchBehaviors.json 

Following show the sample content of SearchBehaviors.json:

```json
[{
  "id": 43, 
  "query_string": "\u6c5f\u6d59\u83dc\u9986 \u5317\u4eac", 
  "origin": "baidu", 
  "time": 1635059303.845, 
  "belong_dialog": 30, 
  "belong_turn": 85, 
  "serp_pagelogs": [
    {
      "id": 903, 
      "url": "https://www.baidu.com/s?wd=%E6%B1%9F%E6%B5%99%E8%8F%9C%E9%A6%86%20%E5%8C%97%E4%BA%AC", 
      "html_name": "serp-903.html", 
      "start_time": 1635059303846, 
      "end_time": 1635059517178, 
      "dwell_time": 174366, 
      "page_id": 1, 
      "clicked_results": "[{\"href\":\"https://www.baidu.com/link?url=6JA9-A-UT3kmslX1Ba5uTZxQmqZxrmpfcvtRkcRj6Ol2-fijyaCtLqiZC8LJ48xm3z2ltG5BMAhTsKWpwZwAy0uAEvh763vXK-RbKoaoOVO&wd=&eqid=9d946fe1000470950000000361750668\",\"type\":\"content\",\"id\":2}]"
    }
  ], 
  "landingpage_pagelogs": [
    {"id": 901, 
     "helpfulness-pagelog": 3, 
     "url": "https://www.zhihu.com/question/21806636/answer/393008334", 
     "html_name": "439.html", 
     "start_time": 1635059315100, 
     "end_time": 1635059515866, 
     "dwell_time": 200766
    }
  ]
}, ......
```

The original HTML files for SERPs and landing pages can be downloaded on the Supplementary part.

