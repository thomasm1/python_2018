// @flow
import React from 'react';
import { findDOMNode } from 'react-dom';

import crypto from 'crypto';

import { map } from 'lodash';

import $ from 'jquery';

export class Select extends React.Component {
  props: {
    data: Array<*>;
    placeholder: string;
    textField?: string|((c:*) => any);
    valueField?: string|((c:*) => any);
    onChange?: Function;
    value?: *;
    label?: string;
  };
  $el: any;
  key: number;
  componentDidMount() {
    this.$el = $(findDOMNode(this));
    this.$el.material_select();
    this.$el.change(
      (e) => this.props.onChange && this.props.onChange(e.target.value));
  }
  componentDidUpdate(prevProps: any) {
    // $FlowIgnore
    const nextKey = crypto.createHash('md5').update(JSON.stringify(this.props.data)).digest("hex");
    if (nextKey !== this.key) {
      this.$el.material_select();
      this.key = nextKey;
    }
  }
  render () {
    let { textField, valueField, placeholder, onChange = (() => null) } = this.props;
    let _textField: Function, _valueField: Function;
    if (typeof textField !== 'function') {
      _textField = (c) => c[textField];
    } else {
      _textField = textField;
    }
    if (typeof valueField !== 'function') {
      _valueField = (c) => c[valueField];
    } else {
      _valueField = valueField;
    }
    return (
      <select
        id={`select-${this.key}`}
        value={this.props.value || ""}
        onChange={this.props.onChange}
      >
        <option value="" disabled>{placeholder}</option>
        {this.props.data.map(
          (option, i) => <option key={`${this.key}-${i}`} value={_valueField(option)}>{_textField(option)}</option>)}
      </select>
    )
  }
}