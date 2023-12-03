import React from "react";
import {Divider, Flex, Layout, theme, Typography} from "antd";
import Search from "antd/es/input/Search";
import styles from "./Main.module.scss";
import Stocks from "./Stocks/Stocks";
import Carousel from "./Carousel/Carousel";
import News from "./News/News";

const {Title, Text} = Typography;

const {Header, Content, Footer, Sider} = Layout;

interface MainPropsType {

}

const Main: React.FC<MainPropsType> = (props) => {
    return (
        <>
            <Stocks/>
            <Divider/>
            <Carousel/>
            <div style={{paddingBottom: 18}}/>
            <News/>
        </>
    );
};

export default Main;
