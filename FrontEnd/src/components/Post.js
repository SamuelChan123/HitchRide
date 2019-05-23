import React from "react";
import PropTypes from "prop-types";

import { withStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import Avatar from "@material-ui/core/Avatar";
import Typography from "@material-ui/core/Typography";
import red from "@material-ui/core/colors/red";

import PostMap from "./PostMap";

const styles = theme => ({
  card: {
    maxWidth: 800,
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-between"
  },
  cardContainer: {},
  media: {
    height: 0,
    paddingTop: "56.25%" // 16:9
  },
  avatar: {
    backgroundColor: red[500]
  },
  mapContainer: {
    height: 200,
    width: 200
  }
});

class Post extends React.Component {
  constructor() {
    super();
    this.state = {
      origin: "College dorm",
      destination: "Dulles Airport",
      time: "May 24 at 3:00pm",
      name: "John Doe",
      originCoords: [51.505, -0.09],
      destinationCoords: [51.555, -0.09]
    };
  }

  render() {
    const { classes } = this.props;
    return (
      <div>
        <Card className={classes.card}>
          <div className={classes.cardContainer}>
            <CardHeader
              avatar={<Avatar aria-label="Name">N</Avatar>}
              title={this.state.name}
              subheader={this.state.time}
            />
            <CardContent>
              <Typography paragraph>Origin: {this.state.origin}</Typography>
              <Typography paragraph>
                Destination: {this.state.destination}
              </Typography>
            </CardContent>
          </div>
          <div id="map-container">
            <PostMap
              origin={this.state.origin}
              destination={this.state.destination}
              originCoords={this.state.originCoords}
              destinationCoords={this.state.destinationCoords}
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
