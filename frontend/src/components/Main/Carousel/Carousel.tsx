import React, {FC} from 'react';
import {Carousel as AntCarousel, Flex, Typography} from 'antd';
import Search from "antd/es/input/Search";

const contentStyle: React.CSSProperties = {
    margin: 0,
    height: '300px',
    color: '#fff',
    textAlign: 'center',
    background: '#000000',
    padding: '10px 100px',
};

const Carousel: FC = () => {
    const onChange = (currentSlide: number) => {
        console.log(currentSlide);
    };

    return (
        <AntCarousel afterChange={onChange} style={{borderRadius: 10, overflow: 'hidden'}}>
            <div>
                <Flex align={'center'} justify={'space-between'} style={contentStyle}>
                    <Typography.Paragraph style={{color: 'white', fontSize: '1.5em', textAlign: "left"}} >
                        Узнай прогноз цен акций компаний, <br />
                        используя <Typography.Text type={'danger'} strong
                                                   style={{fontSize: '1em'}}>AI</Typography.Text> биржу.
                    </Typography.Paragraph>
                    <Search width={300} style={{maxWidth: 400}}/>
                </Flex>
            </div>
            <div>
                <Flex align={'center'} justify={'space-between'} style={contentStyle}>
                    <Typography.Paragraph style={{color: 'white', fontSize: '1.5em', textAlign: "left"}} >
                        Узнай прогноз цен акций компаний, <br />
                        используя <Typography.Text type={'danger'} strong
                                                   style={{fontSize: '1em'}}>AI</Typography.Text> биржу.
                    </Typography.Paragraph>
                    <Search width={300} style={{maxWidth: 400}}/>
                </Flex>
            </div>
            <div>
                <Flex align={'center'} justify={'space-between'} style={contentStyle}>
                    <Typography.Paragraph style={{color: 'white', fontSize: '1.5em', textAlign: "left"}} >
                        Узнай прогноз цен акций компаний, <br />
                        используя <Typography.Text type={'danger'} strong
                                                   style={{fontSize: '1em'}}>AI</Typography.Text> биржу.
                    </Typography.Paragraph>
                    <Search width={300} style={{maxWidth: 400}}/>
                </Flex>
            </div>
            <div>
                <Flex align={'center'} justify={'space-between'} style={contentStyle}>
                    <Typography.Paragraph style={{color: 'white', fontSize: '1.5em', textAlign: "left"}} >
                        Узнай прогноз цен акций компаний, <br />
                        используя <Typography.Text type={'danger'} strong
                                                   style={{fontSize: '1em'}}>AI</Typography.Text> биржу.
                    </Typography.Paragraph>
                    <Search width={300} style={{maxWidth: 400}}/>
                </Flex>
            </div>
        </AntCarousel>
    );
};

export default Carousel;
