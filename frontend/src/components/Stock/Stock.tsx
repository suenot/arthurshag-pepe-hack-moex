import React, {FC, useEffect, useState} from 'react';
import {Avatar, Card, Col, Flex, Row, Space, Typography} from 'antd';
import Search from "antd/es/input/Search";
import Chart from "./Chart";
import {mainApi} from "../../api/Api";
import {useParams} from "react-router-dom";

const Stock: FC = () => {
    const [dataCard, setDataCard] = useState<any>(null);
    const id = useParams().id;
    useEffect(() => {
        if (!id)
            return;
        mainApi.getStock(id as any).then((data) => {
            setDataCard(data || {} as any[]);
        });
    }, [id])

    function onChangeSearch(e: typeof Search.arguments.onChange) {
        setDataCard(e.target.value);
    }

    if (!dataCard)
        return <></>;
    return (
        <Space size={'large'} direction={"vertical"} style={{width: '100%'}}>
            <Card bordered={true} size={"small"}
                  style={{boxShadow: '0px 4px 4px 0px rgba(0, 0, 0, 0.25)', padding: '24px 64px'}}
                  bodyStyle={{padding: 0}}
            >
                <Flex vertical
                      gap={'small'}>
                    <Typography.Title level={2} style={{margin: 0}}>Прогноз</Typography.Title>
                    <Typography.Text style={{marginBottom: 4, fontWeight: 300}}>Напишите название интересующей
                        компании</Typography.Text>
                    <Search allowClear style={{width: 200}}/>
                </Flex>
            </Card>

            <Card bordered={true} size={"small"}
                  style={{boxShadow: '0px 4px 4px 0px rgba(0, 0, 0, 0.25)', padding: '36px 62px', marginBottom: 10}}
                  bodyStyle={{padding: 0}}
            >
                <Row>
                    <Col span={11}>
                        <Card bordered={true} size={"small"}
                              style={{
                                  background: dataCard.background,
                                  width: 450,
                                  marginBottom: 70,
                                  padding: '24px 28px'
                              }}
                              bodyStyle={{padding: 0}}
                        >
                            <Flex gap={28}>
                                <Avatar
                                    style={{alignSelf: 'center', flex: '0 0 auto'}}
                                    size={{xs: 24, sm: 32, md: 40, lg: 64, xl: 80, xxl: 94}}
                                    src={dataCard.companyIcon}
                                />
                                <Flex style={{color: 'white', minWidth: 0, width: '100%', flex: '1 1 auto'}} vertical>
                                    <p style={{
                                        fontSize: '32px',
                                        fontWeight: '600',
                                        whiteSpace: 'nowrap',
                                        textOverflow: 'ellipsis',
                                        overflow: 'hidden'
                                    }}>{dataCard.companyName}</p>
                                    <p style={{fontSize: '16px', fontWeight: '500'}}>Сектор</p>
                                    <p style={{fontSize: '18px'}}>
                                        Финансовый
                                    </p>
                                </Flex>
                            </Flex>
                        </Card>

                        <Chart/>

                    </Col>
                    <Col offset={2} span={12} style={{maxWidth: 425}}>
                        <div style={{paddingBottom: 20}}>
                            <p style={{fontSize: '20px', fontWeight: '500', marginBottom: 16}}>О
                                компании {dataCard.companyName}</p>
                            <p style={{fontSize: '12px', fontWeight: '500'}}>{dataCard.description}</p>
                        </div>
                        <div>
                            <h2 style={{paddingBottom: 16}}>Сводный прогноз</h2>
                            <Space direction={'vertical'} size={'large'} style={{width: '100%'}}>
                                <div style={{padding: '12px 16px', border: 'solid 1px black', borderRadius: 8}}>
                                    <p>Прогнозная цена на час</p>
                                    <p>{dataCard.forecast.hour.price} + {dataCard.forecast.hour.price * dataCard.forecast.hour.changePercentage / 100} ₽
                                        ({dataCard.forecast.week.changePercentage}%)</p>
                                </div>

                                <div style={{padding: '12px 16px', border: 'solid 1px black', borderRadius: 8}}>
                                    <p>Прогнозная цена на день</p>
                                    <p>{dataCard.forecast.day.price} + {dataCard.forecast.day.price * dataCard.forecast.day.changePercentage / 100} ₽
                                        ({dataCard.forecast.week.changePercentage}%)</p>
                                </div>

                                <div style={{padding: '12px 16px', border: 'solid 1px black', borderRadius: 8}}>
                                    <p>Прогнозная цена на неделю</p>
                                    <p>{dataCard.forecast.week.price} + {dataCard.forecast.week.price * dataCard.forecast.week.changePercentage / 100} ₽
                                        ({dataCard.forecast.week.changePercentage}%)</p>
                                </div>
                            </Space>
                        </div>
                    </Col>
                </Row>
            </Card>
        </Space>
    );
};

export default Stock;
