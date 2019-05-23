import React from "react";
import { Map, TileLayer, Marker, Popup } from "react-leaflet";

class PostMap extends React.Component {
  constructor() {
    super();
    this.state = {
      zoom: 10
    };
  }
  render() {
    return (
      <Map
        center={this.props.originCoords}
        zoom={this.state.zoom}
        bounds={[this.props.originCoords, this.props.destinationCoords]}
      >
        <TileLayer
          attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
          url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
        />
        <Marker position={this.props.originCoords}>
          <Popup>{this.props.origin}</Popup>
        </Marker>
        <Marker position={this.props.destinationCoords}>
          <Popup>{this.props.destination}</Popup>
        </Marker>
      </Map>
    );
  }
}

export default PostMap;
