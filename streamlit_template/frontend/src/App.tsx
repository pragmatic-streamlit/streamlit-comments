import React from "react";
import { withStreamlitConnection, StreamlitComponentBase, ComponentProps, Streamlit } from 'streamlit-component-lib';

export enum StreamlitEventType {

}

export interface StreamlitEvent {
  type: StreamlitEventType;
}

export const noticeStreamlit = (event: StreamlitEvent) =>
  Streamlit.setComponentValue(event)

interface IProps {

}

interface IState {

}

class CustomStreamlitComponent extends StreamlitComponentBase<IState> {
  private args: IProps;

  constructor(props: ComponentProps) {
    super(props);
    this.args = props.args;
    this.state = {

    }
  }
  

  public render(): React.ReactNode {
    return (
      <div>your code</div>
    )
  }
}

export default withStreamlitConnection(CustomStreamlitComponent);
