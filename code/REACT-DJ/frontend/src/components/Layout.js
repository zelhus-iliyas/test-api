import React, {useEffect} from 'react'
import Navbar from "./Navbar";
import {googleAuthenticate} from "../actions/auth";
import {connect} from "react-redux";
import {useLocation} from "react-router-dom";
import queryString from "query-string";

const Layout = (props) => {
    const location = useLocation()
    useEffect(() => {
        const values = queryString.parse(location.search)
        const state = values.state ? values.state : null
        const code = values.code ? values.code : null
        console.log('State: '+ state)
        console.log('Code: '+code)
        if (state && code){
            props.googleAuthenticate(state, code)
        }
    }, [location])

    return (
        <div className="container">
            <Navbar/>

            {props.children}
        </div>
    )
}

export default connect(null, { googleAuthenticate})(Layout)