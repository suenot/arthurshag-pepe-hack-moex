import React, {FC} from 'react';
import {Card, Divider, Flex, Image, Typography} from 'antd';
import {useNavigate} from "react-router-dom";
import styles from "./News.module.scss";

const NewsItem: FC = () => {
    const navigate = useNavigate();

    function onClick(): void {
    }

    return (
        <Flex flex="1 1 242px">
            <Card bordered={true} size={"small"}
                  hoverable={true}
                  className={styles.newsItem}
                  style={{boxShadow: '0px 4px 4px 0px rgba(0, 0, 0, 0.25)', paddingBottom: 0}}
                  bodyStyle={{padding: 0}}
                  onClick={onClick}
                  cover={<img
                      height={124}
                      src="https://img.freepik.com/premium-vector/growth-arrow-financial-graph-on-digital-technology-strategy-background_701664-107.jpg"
                  />}
            >
                <Flex vertical style={{paddingBottom: 30, paddingLeft: 12, paddingRight: 12, paddingTop: 10}}>
                    <Typography.Text style={{fontSize: 11, paddingBottom: 9}}>11 ноября</Typography.Text>
                    <Typography.Text strong style={{fontSize: 13, paddingBottom: 16}}>Новость</Typography.Text>
                    <Typography.Text style={{fontSize: 11}}>Че-то произошло, где-то там и че-то случилось дальше вооот</Typography.Text>
                </Flex>
            </Card>
        </Flex>
    );
};

export default NewsItem;
