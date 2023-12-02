import React, {FC} from 'react';
import {Card, Divider, Flex, Space, Typography} from 'antd';
import NewsItem from "./NewsItem";


const News: FC = () => {
    return (
        <Space direction={"vertical"}>
            <Typography.Title level={2}>Лента</Typography.Title>
            <Flex gap={"small"}>
                <NewsItem />
                <NewsItem />
                <NewsItem />
                <NewsItem />
            </Flex>
        </Space>
    );
};

export default News;
