import React, {FC} from 'react';
import {Card, Col, Divider, Flex, Row, Typography} from "antd";
import styles from "./Stocks.module.scss";
import {RedditOutlined} from "@ant-design/icons";


interface PropsType {
    id: number;
    text: string;
}

const Stock: FC<PropsType> = ({id, text}) => {
    return (
        <Card className={styles.card} bordered={true} size={"small"} >
            <Flex vertical align={'center'}>
                <Typography.Text strong><span>{text || 'Пивнуха'}</span> <Typography.Text type={'success'}>+ 1.2%</Typography.Text></Typography.Text>
                <Divider style={{margin: '5px 0'}}/>
                <Typography.Text>
                    <RedditOutlined/> ГЗП
                </Typography.Text>
            </Flex>
        </Card>
    );
};

export default Stock;
