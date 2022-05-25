# ConvSearch Dataset
This repository is the home of the  **C**hinese **O**pen-Domai**n** Con**v**ersational **Search** Behavior Dataset (ConvSearch). You can refer to paper [ConvSearch: A Open-Domain Conversational Search Behavior Dataset](https://arxiv.org/pdf/2204.02659.pdf) for more details on dataset construction and analysis.



## Download data

Our dataset contains the following parts:

- Dialogues (Main part): information of dialogue and corresponding turns, including content, timestamp, annotation results, et al.
- Agent behaviors (Main part): the information seeking behaviors of agent before they respond to users, including query requests, SERPs with click action, landing pages.
- The HTML files of SERPs (search engine result pages) and landing pages in agent search behavior (Supplementary part).
- Image files in dialogues (Supplementary part).



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

