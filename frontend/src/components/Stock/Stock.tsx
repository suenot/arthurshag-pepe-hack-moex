import React, {FC} from 'react';
import {Avatar, Card, Col, Flex, Image, Row, Space, Typography} from 'antd';
import Search from "antd/es/input/Search";

const Stock: FC = () => {
    return (
        <Space size={'middle'} direction={"vertical"} style={{width: '100%'}}>
            <Card bordered={true} size={"small"}
                  style={{boxShadow: '0px 4px 4px 0px rgba(0, 0, 0, 0.25)'}}
            >
                <Flex vertical style={{paddingBottom: 20, paddingTop: 20, paddingLeft: 12, paddingRight: 12}}
                      gap={'small'}>
                    <Typography.Title level={2} style={{margin: 0}}>Прогноз</Typography.Title>
                    <Typography.Text>Напишите название интересующей компании</Typography.Text>
                    <Search allowClear style={{width: 200}}/>
                </Flex>
            </Card>

            <Card bordered={true} size={"small"}
                  style={{boxShadow: '0px 4px 4px 0px rgba(0, 0, 0, 0.25)'}}
            >
                <Row>
                    <Col span={12}>
                        <Card bordered={true} size={"small"}
                              style={{boxShadow: '0px 4px 4px 0px rgba(0, 0, 0, 0.25)', background: "#00AE11"}}
                        >
                            <Flex gap={"middle"}>
                                <Avatar
                                    size={{xs: 24, sm: 32, md: 40, lg: 64, xl: 80, xxl: 100}}
                                    src={"https://cdn.tvspb.ru/storage/wp-content/uploads/2022/06/sber-vk-3mdthumbnail_gyFF4eN.jpg__0_0x0.jpg"}
                                />
                                <Flex style={{color: 'white'}} vertical>
                                    <p style={{fontSize: '32px', fontWeight: '600'}}>СБЕР БАНК</p>
                                    <p style={{fontSize: '16px', fontWeight: '500'}}>Сектор</p>
                                    <p style={{fontSize: '18px'}}>
                                        Финансовый
                                    </p>
                                </Flex>
                            </Flex>
                        </Card>
                    </Col>
                    <Col span={12}>123</Col>
                </Row>
            </Card>
        </Space>
    );
};

export default Stock;
