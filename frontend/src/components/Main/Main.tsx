import React from "react";
import {useFormik} from "formik";
import {Button, Card, Col, Divider, Flex, Grid, Input, Row, Typography} from "antd";
import {Breadcrumb, Layout, Menu, theme} from 'antd';
import Search from "antd/es/input/Search";
import styles from "./Main.module.scss";

const {Title, Text} = Typography;

const {Header, Content, Footer, Sider} = Layout;

interface MainPropsType {

}

const Main: React.FC<MainPropsType> = (props) => {
    const {
        token: {colorBgContainer},
    } = theme.useToken();
    return (
        <Layout className="layout">
            <Sider collapsible collapsed={true}>
                <div className="demo-logo-vertical"/>
            </Sider>
            <Layout style={{padding: '10px 30px'}}>
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
                    <Row className={styles.list}>
                        {['', '', '', '', '','', '', '', '', ''].map(() => {
                            return <Col span={2}>
                                <Card className={styles.card}>Талон в пивнуху</Card>
                            </Col>
                        })}
                    </Row>
                    <Flex gap={5}>
                        <Card className={styles.card} bordered={true} size={"small"}>Дым</Card>
                        <Card className={styles.card} bordered={true} size={"small"}>Дымоок</Card>
                        <Card className={styles.card} bordered={true} size={"small"}>Зашол на посашок</Card>
                    </Flex>
                </Content>
                <Footer style={{textAlign: 'center'}}>ООО Дымный Татар интертеймент</Footer>
            </Layout>
        </Layout>
    );
};

export default Main;
