        import React from 'react';
        import ReactDOM from 'react-dom';
        import PubSub from 'pubsub-js';
        import $ from 'jquery';
        import Bootstrap from 'bootstrap/dist/css/bootstrap.css';

        import EventBox from "./event-box"



ReactDOM.render(
  <EventBox url="/api/events" deleteUrl="/api/events/delete" editUrl="api/events/edit" pollInterval={10000} event_types={event_types_loaded} />,
  document.getElementById('chelis_content')
);    
