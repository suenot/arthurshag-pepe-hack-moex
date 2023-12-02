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
    const {
        token: {colorBgContainer},
    } = theme.useToken();
    return (
        <Layout className={styles.main}>
            <Sider collapsible collapsed={true}>
                <div className="demo-logo-vertical"/>
            </Sider>
            <Layout className={styles.content} style={{padding: '33px 150px'}}>
                <Flex gap={5} justify={"space-between"}>
                    <Search allowClear style={{width: 200}}/>
                    <Flex gap={10}>
                        <Typography>10:04 (GMT +3:00)</Typography>
                        <Typography>30 ноября 2023</Typography>
                        <Typography>Илья Бочонок Пива</Typography>
                    </Flex>
                </Flex>
                <Divider/>

                <Content>
                    <Stocks/>
                    <Divider/>
                    <Carousel />
                    <div style={{paddingBottom: 18}}/>
                    <News />
                </Content>
                <Footer style={{textAlign: 'center'}}>ООО Дымный Татар интертеймент</Footer>
            </Layout>
        </Layout>
    );
};

export default Main;
