import React from "react";
import PropTypes from "prop-types";

import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import InputBase from '@material-ui/core/InputBase';
import { fade } from '@material-ui/core/styles/colorManipulator';
import { withStyles } from '@material-ui/core/styles';



const styles = theme => ({
  root: {
    width: '100%',
  },
  grow: {
    flexGrow: 1,
  },
  menuButton: {
    marginLeft: -12,
    marginRight: 20,
  },
  title: {
    display: 'none',
    [theme.breakpoints.up('sm')]: {
      display: 'block',
    },
  },
  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: fade(theme.palette.common.white, 0.15),
    '&:hover': {
      backgroundColor: fade(theme.palette.common.white, 0.25),
    },
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing.unit,
      width: 'auto',
    },
  },
  searchIcon: {
    width: theme.spacing.unit * 9,
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inputRoot: {
    color: 'inherit',
    width: '100%',
  },
  inputInput: {
    paddingTop: theme.spacing.unit,
    paddingRight: theme.spacing.unit,
    paddingBottom: theme.spacing.unit,
    paddingLeft: theme.spacing.unit,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      width: 120,
      '&:focus': {
        width: 200,
      },
    },
  },
});

class Header extends React.Component {
  render() {
    const { classes } = this.props;
    return (
      <div className={classes.root}>
        <AppBar position="static">
          <Toolbar>
            <IconButton className={classes.menuButton} color="inherit" aria-label="Open drawer">
            </IconButton>
            <Typography className={classes.title} variant="h4" color="inherit" noWrap>
              <b>HitchRide</b>
            </Typography>
            <div className={classes.grow} />
            <div className={classes.search}>
              <InputBase
                placeholder="Origin"
                classes={{
                  root: classes.inputRoot,
                  input: classes.inputInput,
                }}
                type="text"
              />
            </div>
            <div className={classes.search}>
              <InputBase
                placeholder="Destination"
                classes={{
                  root: classes.inputRoot,
                  input: classes.inputInput,
                }}
                type="text"
              />
            </div>
            <div className={classes.search}>
              <InputBase
                placeholder="Departure Date"
                classes={{
                  root: classes.inputRoot,
                  input: classes.inputInput,
                }}
                type="date"
              />
            </div>
            <div className={classes.search}>
              <InputBase
                placeholder="Departure Time"
                classes={{
                  root: classes.inputRoot,
                  input: classes.inputInput,
                }}
                type="time"
              />
            </div>

          </Toolbar>
        </AppBar>
      </div>
    );
  }
}

Header.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(Header);
