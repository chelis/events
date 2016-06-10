/*
* @Author: Marcela Campo
* @Date:   2016-05-31 20:18:13
* @Last Modified by:   Marcela Campo
* @Last Modified time: 2016-05-31 20:27:37
*/

import React from 'react';
import ReactDOM from 'react-dom';
import PubSub from 'pubsub-js';
import Bootstrap from 'bootstrap/dist/css/bootstrap.css';


        var EditButton = React.createClass({
            handleClick: function(){
               PubSub.publish('edit', this.props.obj);
            },
            render: function() {
                return(<a href="#" onClick={this.handleClick}>Editar </a>)
            }
        })
        var DeleteButton = React.createClass({
            handleClick: function(){
              this.props.callback(this.props.obj)  
            },
            render: function() {
                return(<a href="#" onClick={this.handleClick}>Borrar </a>)
            }
        })

        var Event = React.createClass({
          rawMarkup: function() {
            var rawMarkup = marked(this.props.children.toString(), {sanitize: true});
            return { __html: rawMarkup };
          }, 
          render: function() {
            
            return (
              <tr className="Event">
                <td className="EventUser">
                  {this.props.event.user}
                </td>
                  <td className="EventType">
                  {this.props.event.event_type_name}
                  </td>
                  <td className="EventNotes">
                  {this.props.event.notes}
                  </td>
                  <td>
                  <DeleteButton callback={this.props.callback} obj={this.props.event.id}/>
                  <EditButton obj={this.props.event}/>
                  </td>
                </tr>
            );
          }
        });    
        var EventList = React.createClass({
          render: function() {
                var onEventDelete = this.props.onEventDelete
                if (this.props.data !=undefined){
                var eventNodes = this.props.data.map(function(event) {
                  return (
                    <Event event={event}  key={event.id} callback={onEventDelete}>
                    </Event>

                  );
                });
              } else {var eventNodes = ''} 

                return (
                  <table className="table table-striped">
                  <thead>
                  <th>User</th>
                  <th>Event Type</th>
                  <th>Notes</th>
                  </thead>
                  <tbody>
                    {eventNodes}
                    </tbody>
                  </table>
                );          
              }
        });

export default EventList;
