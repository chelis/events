/*
* @Author: Marcela Campo
* @Date:   2016-05-31 20:19:53
* @Last Modified by:   Marcela Campo
* @Last Modified time: 2016-05-31 20:26:33
*/

import React from 'react';
import ReactDOM from 'react-dom';
import PubSub from 'pubsub-js';



        var EventForm = React.createClass({
          getInitialState: function() {
              
              var options = this.props.event_types.map(function(elem){
                    return (<option  key={elem.id} value={elem.id}>{elem.name}</option>);
                  });
              options.unshift(<option  key='-1' value='-1'>---------------</option>)
              return {user: '', notes: '', event_type:'', event_type_options: options, editing:null};
            },

            componentWillMount: function() {
                // when React renders me, I subscribe to the topic 'products'
                // .subscribe returns a unique token necessary to unsubscribe
                this.pubsub_token = PubSub.subscribe('edit', function(e, elem) {
                  // update my selection when there is a message
                  this.toggleEditing(elem);
                }.bind(this));
              },

              componentWillUnmount: function() {
                // React removed me from the DOM, I have to unsubscribe from the pubsub using my token
                PubSub.unsubscribe(this.pubsub_token);
              },

            toggleEditing: function(elem){
                this.setState({editing: elem.id, user:elem.user, notes:elem.notes, event_type:elem.event_type}) 
                this.render()
            },
            handleEventTypeChange: function(e) {
              this.setState({event_type: e.target.value});
              var index = e.nativeEvent.target.selectedIndex;
              var option_text = e.nativeEvent.target[index].text              
              this.setState({event_type_name: option_text});
            },

            handleUserChange: function(e) {
              this.setState({user: e.target.value});
            },
            handleNotesChange: function(e) {
              this.setState({notes: e.target.value});
            },          
            handleSubmit: function(e) {
              e.preventDefault();
              var user = this.state.user.trim();
              var notes = this.state.notes.trim();
              var event_type = this.state.event_type
              var event_type_name = this.state.event_type_name

              if (!notes || !user || !event_type) {
                return;
              }
              
              if (this.state.editing == null) {
                console.log(this.state.editing)
                this.props.onEventSubmit({user: user, notes: notes, event_type:event_type, event_type_name:event_type_name});
              } else {
                this.props.onEventEdit({id: this.state.editing, user: user, notes: notes, event_type:event_type, event_type_name:event_type_name});
              }
              this.setState({user: '', notes: '', event_type:'', event_type_name:'-1', editing:null});
            },            
          render: function() {
            return (
                <form className="eventForm" onSubmit={this.handleSubmit}>
                  <input type="text" placeholder="Your name"  value={this.state.user}
                          onChange={this.handleUserChange}/>
                  <input type="text" placeholder="Say something..."   value={this.state.notes}
                          onChange={this.handleNotesChange}/>
                  <select placeholder="Select event type...." value={this.state.event_type} onChange={this.handleEventTypeChange}>
                      {this.state.event_type_options}
                  </select>
                  <input type="submit" value="Post" />
                </form>
            );
          }
        });    


export default EventForm
