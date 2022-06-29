// import { LEFT_NAVIGATION_BAR_WIDTH } from '@components/LeftNavigationBar/Style'
import styled, { keyframes } from 'styled-components'

export const Container = styled.div`
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(34, 34, 34, 0.6);
  z-index: 1000;
  display: flex;
  justify-content: center;
  align-items: center;
`

const Loading = keyframes`
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }`

export const LoadingComponent = styled.div`
  display: inline-block;
  width: 50px;
  height: 50px;
  :after {
    content: ' ';
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 10px solid #fff;
    border-color: #fff transparent #fff transparent;
    -webkit-animation: ${Loading} 1.1s infinite linear;
    animation: ${Loading} 1.1s infinite linear;
  }
`
