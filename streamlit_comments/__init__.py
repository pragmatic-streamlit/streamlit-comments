
import os
from datetime import datetime
import streamlit.components.v1 as components
from typing import Optional, Union, Dict, List
from dataclasses import dataclass, field
import streamlit as st

_DEVELOP_MODE = os.getenv('DEVELOP_MODE')
# _DEVELOP_MODE = True

if _DEVELOP_MODE:
    _component_func = components.declare_component(
        "streamlit-comments",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component("streamlit-comments", path=build_dir) # noqa

@dataclass
class CommentDataProps:
  userId: str = field(default="")
  comId: str = field(default="")
  fullName: str = field(default="")
  createdTime: int = field(default=datetime.now)
  avatarUrl: Optional[str] = field(default=None)
  text: str = field(default="")
  userProfile: Optional[str] = field(default=None)
  parentId: Optional[str] = field(default=None)
  replies: "List[CommentDataProps]" = field(default_factory=list)


def st_comments(
    currentUserId: str,
    currentUserFullName: str,
    currentUserImg: str = None,
    currentUserProfile: str = None,
    replyTop: bool = False,
    customImg: str = None,
    inputStyle: Dict = None,
    formStyle: Dict = None,
    submitBtnStyle: Dict = None,
    cancelBtnStyle: Dict = None,
    overlayStyle: Dict = None,
    imgStyle: Dict = None,
    replyInputStyle: Dict = None,
    commentsCount: int = None,
    hrStyle: Dict = None,
    titleStyle: Dict = None,
    removeEmoji: bool= False,
    advancedInput: bool = False,
    commentData: List[CommentDataProps] = [],
    allowDelete: bool = False,
    allowEdit: bool = False,
    customNoComment: str = None,
    key = None,
):
    user_info = {
        "currentUserId": currentUserId,
        "currentUserFullName": currentUserFullName,
        "currentUserImg": currentUserImg,
        "currentUserProfile": currentUserProfile,
    }
    
    current_user_info = {}
    for item in user_info:
        if user_info[item] is None:
            continue
        current_user_info[item] = user_info[item]

    params = {
        "currentUser": current_user_info,
        "replyTop": replyTop,
        "customImg": customImg,
        "inputStyle": inputStyle,
        "formStyle": formStyle,
        "submitBtnStyle": submitBtnStyle,
        "cancelBtnStyle": cancelBtnStyle,
        "overlayStyle": overlayStyle,
        "imgStyle": imgStyle,
        "replyInputStyle": replyInputStyle,
        "commentsCount": commentsCount,
        "hrStyle": hrStyle,
        "titleStyle": titleStyle,
        "removeEmoji": removeEmoji,
        "advancedInput": advancedInput,
        "commentData": commentData,
        "allowDelete": allowDelete,
        "allowEdit": allowEdit,
        "customNoComment": customNoComment,
    }
    
    current_params = {}
    for item in params:
        if params[item] is None:
            continue
        current_params[item] = params[item]

    event = _component_func(key=key, **current_params)
    
    STREAMLIT_FRONTEND_MESSAGE_ID_KEY = "streamlit_frontend_message_id"

    if st.session_state.get(STREAMLIT_FRONTEND_MESSAGE_ID_KEY, None) is None:
        st.session_state[STREAMLIT_FRONTEND_MESSAGE_ID_KEY] = {}

    if event:
        id = event.get("id", None)
        if not id:
            return None
        if id in st.session_state[STREAMLIT_FRONTEND_MESSAGE_ID_KEY]:
            return None
        st.session_state[STREAMLIT_FRONTEND_MESSAGE_ID_KEY][id] = True
    return event


if _DEVELOP_MODE:
    
    test_data = [
        {
            "userId": "01a",
            "comId": "012",
            "fullName": "Riya Negi",
            "text": "Hey, Loved your blog! ",
            "createdTime": 1688646541266,
            "replies": [
                {
                    "userId": "02a",
                    "comId": "013",
                    "fullName": "Adam Scott",
                    "createdTime": 1688646541266,
                    "text": "Thanks! It took me 1 month to finish this project but I am glad it helped out someone!🥰",
                    "replies": [
                        {
                            "userId": "05a",
                            "comId": "020",
                            "fullName": "aaaaa",
                            "createdTime": 1688646541266,
                            "text": "test",
                        }
                    ]
                },
                {
                    "userId": "01a",
                    "comId": "014",
                    "fullName": "Riya Negi",
                    "text": "thanks!😊",
                    "createdTime": 1688646541266,
                }
            ]
            },
        {
            "userId": "02b",
            "comId": "017",
            "fullName": "Lily",
            "text": "I have a doubt about the 4th point🤔",
            "replies": [],
            "createdTime": 1688646541266,
        }
    ]
    
    st.write("## Default Comments")
    event = st_comments(
        key="test",
        currentUserId="01a",
        currentUserFullName="Riya Negi",
        titleStyle={ "display": "none" },
        hrStyle={ "display": "none" },
        commentData=[],
        customNoComment=" ",
    )
    print(111, event)
    st.write(event)
    
    
    st.write("## Class Comments")
    event = st_comments(
        key="test2",
        currentUserId="01a",
        currentUserFullName="Riya Negi",
        commentData=test_data,
    )
    st.write(event)
    
    
    st.write("## Custom Comments")
    event = st_comments(
        key="test3",
        currentUserId="01a",
        currentUserFullName="Riya Negi",
        currentUserImg="https://ui-avatars.com/api/name=Riya&background=random",
        hrStyle={ "border": '0.5px solid #ff0072' },
        titleStyle={ "color": '#f2f2f2' },
        commentsCount=5,
        commentData=test_data,
        imgStyle={ "borderRadius": '0%' },
        customImg='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F13%2F2015%2F04%2F05%2Ffeatured.jpg&q=60',
        inputStyle={ "border": '1px solid rgb(208 208 208)' },
        formStyle={ "backgroundColor": 'white' },
        submitBtnStyle={ "border": '1px solid black', "backgroundColor": 'black' },
        cancelBtnStyle={
          "border": '1px solid gray',
          "backgroundColor": 'gray',
          "color": 'white',
        },
        removeEmoji=True,
        overlayStyle={ "backgroundColor": '#0f0d29', "color": 'white' },
        replyInputStyle={ "borderBottom": '1px solid black', "color": 'black' },
    )
    st.write(event)
    
    
    st.write("## Advanced Comments")
    event = st_comments(
        key="test4",
        currentUserId='01a',
        currentUserImg='https://ui-avatars.com/api/name=Riya&background=random',
        currentUserFullName='Riya Negi',
        hrStyle={ "border": '0.5px solid #ff0072' },
        commentData=test_data,
        customImg='https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F13%2F2015%2F04%2F05%2Ffeatured.jpg&q=60',
        inputStyle={ "border": '1px solid rgb(208 208 208)' },
        formStyle={ "backgroundColor": 'white' },
        submitBtnStyle={
          "border": '1px solid black',
          "backgroundColor": 'black',
          "padding": '7px 15px',
        },
        cancelBtnStyle={
          "border": '1px solid gray',
          "backgroundColor": 'gray',
          "color": 'white',
          "padding": '7px 15px'
        },
        advancedInput=True,
        replyInputStyle={ "borderBottom": '1px solid black', "color": 'black' },
    )
    
