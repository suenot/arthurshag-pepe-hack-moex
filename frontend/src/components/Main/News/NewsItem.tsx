import React, {FC} from 'react';
import {Card, Divider, Flex, Image, Typography} from 'antd';

const NewsItem: FC = () => {

    return (
        <Flex flex="0 0 252px">
            <Card bordered={true} size={"small"}
                  style={{boxShadow: '0px 4px 4px 0px rgba(0, 0, 0, 0.25)'}}
                  cover={<Image
                      src="https://sun9-52.userapi.com/impg/6f8oFAmeOlA-z3RJdpR2iMTwVCicihSRmP9Wmg/Mlh8K8v5tRU.jpg?size=960x384&quality=96&sign=7f70800ec594d3206103dbfcd76a9d65&type=album"
                  />}
            >
                <Flex vertical style={{paddingBottom: 38, paddingLeft: 12, paddingRight: 12, paddingTop: 10}}>
                    <Typography.Text>11 ноября</Typography.Text>
                    <Typography.Text strong>Готовилось нападение</Typography.Text>
                    <Typography.Text>Lorem ipsum dolor sit amet</Typography.Text>
                </Flex>
            </Card>
        </Flex>
    );
};

export default NewsItem;
