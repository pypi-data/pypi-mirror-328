import { ReactWidget } from '@jupyterlab/apputils'
import React from 'react'
import { VariablePanel } from './variablePanel';
import { NotebookPanel } from '@jupyterlab/notebook';
import { VariableRefreshContextProvider } from '../context/variableRefershContext';

export interface VariablePanelWidgetProps {
  variableName: string;
  variableType: string;
  variableData: any[];
  notebookPanel?: NotebookPanel | null;
}

export class VariablePanelWidget extends ReactWidget {

  constructor(private props: VariablePanelWidgetProps) {
    super();
    this.update();
  }

  protected render(): JSX.Element {
    return (
      <div style={{ height: '100%', width: '100%'}}>
      <VariableRefreshContextProvider notebookPanel={this.props.notebookPanel}>
      <VariablePanel variableName={this.props.variableName}
        variableType={this.props.variableType}
        variableData={this.props.variableData}
        notebookPanel={this.props.notebookPanel}
        />
      </VariableRefreshContextProvider>
      </div>
    )
  }

}
