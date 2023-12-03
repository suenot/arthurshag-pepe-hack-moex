import React from "react";
import {Divider, Flex, Layout as LayoutAnt, theme, Typography} from "antd";
import Search from "antd/es/input/Search";
import styles from "./Layout.module.scss";
import Main from "../Main/Main";
import {Route, Routes } from "react-router-dom";
import Stock from "../Stock/Stock";


const {Header, Content, Footer, Sider} = LayoutAnt;

interface PropsType {

}

const Layout: React.FC<PropsType> = () => {
    const {
        token: {colorBgContainer},
    } = theme.useToken();
    return (
        <LayoutAnt className={styles.main}>
            <Sider collapsible collapsed={true}>
                <div className="demo-logo-vertical"/>
            </Sider>
            <LayoutAnt className={styles.content} style={{padding: '33px 150px'}}>
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
                    <Routes>
                        <Route path="" element={<Main />} />
                        <Route path="card" element={<Stock />} />
                    </Routes>
                </Content>
                <Footer style={{textAlign: 'center'}}>ООО Дымный Татар интертеймент</Footer>
            </LayoutAnt>
        </LayoutAnt>
    );
};

export default Layout;
