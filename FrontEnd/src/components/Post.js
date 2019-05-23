import React from "react";
import PropTypes from "prop-types";

import { withStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import Avatar from "@material-ui/core/Avatar";
import Typography from "@material-ui/core/Typography";

import PostMap from "./PostMap";

const styles = theme => ({
  card: {
    width: 800,
    margin: "10px",
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-between"
  },
  mapContainer: {
    height: 200,
    width: 200
  }
});

class Post extends React.Component {
  constructor() {
    super();
    this.state = {};
  }

  render() {
    const { classes } = this.props;
    return (
      <div>
        <Card className={classes.card}>
          <div>
            <CardHeader
              avatar={
                <Avatar aria-label="Name">
                  {this.props.name[0] +
                    this.props.name
                      .trim()
                      .split(" ")
                      .slice(-1)[0][0]
                      .toUpperCase()}
                </Avatar>
              }
              title={this.props.name}
              subheader={this.props.time}
            />
            <CardContent>
              <Typography paragraph>Origin: {this.props.origin}</Typography>
              <Typography paragraph>
                Destination: {this.props.destination}
              </Typography>
            </CardContent>
          </div>
          <div id="map-container">
            <PostMap
              origin={this.props.origin}
              destination={this.props.destination}
              originCoords={this.props.originCoords}
              destinationCoords={this.props.destinationCoords}
            />
          </div>
        </Card>
      </div>
    );
  }
}

Post.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Post);
