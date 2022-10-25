import React,{Component} from "react";
import CreateRoomPage from "./CreateRoomPage";
import RoomJoinPage from "./RoomJoinPage";
import {BrowerRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";



export default class HomePage extends Component{

    constructor(props){
        super(props);
    }


    render(){
        return (
            <div>
            <HomePage />
            <RoomJoinPage />
            <CreateRoomPage />
            </div>
        );
        
            
    }
}