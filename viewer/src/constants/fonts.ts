import styled, { css } from 'styled-components'

const Text = styled.div<{ color?: string; margin?: string }>`
  font-family: Pretendard;
  font-style: normal;
  font-weight: 500;
  letter-spacing: -0.5px;
  font-feature-settings: 'pnum' on, 'lnum' on;
  ${(props) =>
    props.color &&
    css`
      color: ${props.color};
    `}
  ${(props) =>
    props.margin &&
    css`
      margin: ${props.margin};
    `}
`

// eslint-disable-next-line import/no-anonymous-default-export
export default {
  Regular: {
    10: styled(Text)`
      font-size: 10px;
      line-height: 12px;
      font-weight: 400;
    `,
    12: styled(Text)`
      font-size: 12px;
      line-height: 16px;
      font-weight: 400;
    `,
    13: styled(Text)`
      font-size: 13px;
      line-height: 18px;
      font-weight: 400;
    `,
    14: styled(Text)`
      font-size: 14px;
      line-height: 20px;
      font-weight: 400;
    `,
    15: styled(Text)`
      font-size: 15px;
      line-height: 23px;
      font-weight: 400;
    `,
    16: styled(Text)`
      font-size: 16px;
      line-height: 24px;
      font-weight: 400;
    `,
    18: styled(Text)`
      font-size: 18px;
      line-height: 24px;
      font-weight: 400;
    `,
    26: styled(Text)`
      font-size: 26px;
      line-height: 36px;
      font-weight: 400;
    `,
  },
  Medium: {
    10: styled(Text)`
      font-size: 10px;
      line-height: 12px;
      font-weight: 500;
    `,
    12: styled(Text)`
      font-size: 12px;
      line-height: 16px;
      font-weight: 500;
    `,
    13: styled(Text)`
      font-size: 13px;
      line-height: 18px;
      font-weight: 500;
    `,
    14: styled(Text)`
      font-size: 14px;
      line-height: 20px;
      font-weight: 500;
    `,
    15: styled(Text)`
      font-size: 15px;
      line-height: 23px;
      font-weight: 500;
    `,
    16: styled(Text)`
      font-size: 16px;
      line-height: 24px;
      font-weight: 500;
    `,
    18: styled(Text)`
      font-size: 18px;
      line-height: 24px;
      font-weight: 500;
    `,
    26: styled(Text)`
      font-size: 26px;
      line-height: 36px;
      font-weight: 500;
    `,
  },
  SemiBold: {
    12: styled(Text)`
      font-size: 12px;
      line-height: 16px;
      font-weight: 600;
    `,
    13: styled(Text)`
      font-size: 13px;
      line-height: 16px;
      font-weight: 600;
    `,
    14: styled(Text)`
      font-size: 14px;
      line-height: 20px;
      font-weight: 600;
    `,
    16: styled(Text)`
      font-size: 16px;
      line-height: 22px;
      font-weight: 600;
    `,
    18: styled(Text)`
      font-size: 18px;
      line-height: 24px;
      font-weight: 600;
    `,
    24: styled(Text)`
      font-size: 24px;
      line-height: 28px;
      font-weight: 600;
    `,
  },
  Bold: {
    12: styled(Text)`
      font-size: 12px;
      line-height: 14px;
      font-weight: 700;
    `,
    14: styled(Text)`
      font-size: 14px;
      line-height: 16px;
      font-weight: 700;
    `,
    16: styled(Text)`
      font-size: 16px;
      line-height: 16px;
      font-weight: 700;
    `,
    18: styled(Text)`
      font-size: 18px;
      line-height: 24px;
      font-weight: 700;
    `,
    20: styled(Text)`
      font-size: 20px;
      line-height: 28px;
      font-weight: 700;
    `,
    23: styled(Text)`
      font-size: 23px;
      line-height: 28px;
      font-weight: 700;
    `,
    24: styled(Text)`
      font-size: 24px;
      line-height: 32px;
      font-weight: 700;
    `,
    28: styled(Text)`
      font-size: 28px;
      line-height: 32px;
      font-weight: 700;
    `,
    34: styled(Text)`
      font-size: 34px;
      line-height: 32px;
      font-weight: 700;
    `,
  },
  placeholder: styled(Text)`
    &::-webkit-input-placeholder {
      color: #828282;
    }
  `,
}
