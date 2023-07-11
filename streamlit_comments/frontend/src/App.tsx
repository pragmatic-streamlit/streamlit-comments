import React from "react";
import { withStreamlitConnection, StreamlitComponentBase, ComponentProps, Streamlit } from 'streamlit-component-lib';
import { CommentSection, CommentSectionProps, CommentDataProps } from 'dp-react-comments-section'
import { v4 as uuidv4 } from 'uuid'
import 'dp-react-comments-section/dist/index.css'

export enum StreamlitEventType {
  COMMENT_SUBMIT = "COMMENT_SUBMIT",
  COMMENT_DELETE = "COMMENT_DELETE",
  COMMENT_EDIT = "COMMENT_EDIT",
  COMMENT_REPLY = "COMMENT_REPLY",
}

export interface StreamlitEvent {
  id: string;
  type: StreamlitEventType;
  data: {
    comment: CommentDataProps;
    all: CommentDataProps[];
  };
}

export const noticeStreamlit = (event: StreamlitEvent) => Streamlit.setComponentValue(event)

interface IProps extends CommentSectionProps {}

interface IState {}

class CustomStreamlitComponent extends StreamlitComponentBase<IState> {
  private args: IProps;

  constructor(props: ComponentProps) {
    super(props);
    this.args = props.args;
  }

  handleCommentSubmit = (comment: CommentDataProps, all: CommentDataProps[]) => {
    noticeStreamlit({
      id: uuidv4(),
      type: StreamlitEventType.COMMENT_SUBMIT,
      data: { comment, all }
    })
  }

  handleCommentDelete = (comment: CommentDataProps, all: CommentDataProps[]) => {
    noticeStreamlit({
      id: uuidv4(),
      type: StreamlitEventType.COMMENT_DELETE,
      data: { comment, all }
    })
  }

  handleCommentEdit = (comment: CommentDataProps, all: CommentDataProps[]) => {
    noticeStreamlit({
      id: uuidv4(),
      type: StreamlitEventType.COMMENT_EDIT,
      data: { comment, all }
    })
  }

  handleCommentReply = (comment: CommentDataProps, all: CommentDataProps[]) => {
    noticeStreamlit({
      id: uuidv4(),
      type: StreamlitEventType.COMMENT_REPLY,
      data: { comment, all }
    })
  }

  public render(): React.ReactNode {
    return (
      <CommentSection
        onDeleteAction={this.handleCommentDelete}
        onEditAction={this.handleCommentEdit}
        onReplyAction={this.handleCommentReply}
        onSubmitAction={this.handleCommentSubmit}
        {...this.args}
      />
    )
  }
}

export default withStreamlitConnection(CustomStreamlitComponent);
