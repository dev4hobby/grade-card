// import { FilterTab, FilterTabType, MainMenuTitle, MainMenuType, SubMenuType } from 'src/types'

export const DATA_TABLE_PAGE_SIZE = 20

export const POPUP_CONTAINER_WIDTH = 512
export const POPUP_CONTAINER_MARGIN = 16

// export const mainMenuTitleList: MainMenuTitle[] = [
//   {
//     key: MainMenuType.HOME,
//     menuTitle: '홈',
//     route: '/',
//   },
//   {
//     key: MainMenuType.ORDER_MANAGEMENT,
//     menuTitle: '주문 관리',
//     subMenuTitleList: [
//       {
//         key: SubMenuType.ALL_ORDER,
//         menuTitle: '전체 주문 목록',
//         route: '/order-list',
//       },
//       {
//         key: SubMenuType.ORDER_DELIVERY,
//         menuTitle: '주문/배송 관리',
//         route: '/order-delivery',
//       },
//       {
//         key: SubMenuType.ORDER_CANCEL,
//         menuTitle: '취소/교환/반품/환불',
//         route: '/order-cancel',
//       },
//     ],
//   },
//   {
//     key: MainMenuType.SETTLEMENT_MANAGEMENT,
//     menuTitle: '정산 관리',
//     subMenuTitleList: [
//       {
//         key: SubMenuType.SETTLEMENT,
//         menuTitle: '정산 목록',
//         route: '/settlement-list',
//       },
//       {
//         key: SubMenuType.ADJUSTMENT,
//         menuTitle: '조정 목록',
//         route: '/adjustment-list',
//       },
//       {
//         key: SubMenuType.PAYMENT,
//         menuTitle: '지급 목록',
//         route: '/payment-list',
//       },
//       {
//         key: SubMenuType.TAX_BILL,
//         menuTitle: '전자 세금 계산서',
//         route: '/tax-bill',
//       },
//     ],
//   },
//   {
//     key: MainMenuType.SUPPLIER_INFO,
//     menuTitle: '공급사 정보',
//     route: '/supplier-info',
//   },
//   {
//     key: MainMenuType.STATISTICS,
//     menuTitle: '통계',
//     route: '/statistics',
//   },
// ]

// export const supplierMainMenuTitleList = mainMenuTitleList.filter(
//   (mainMenu) => mainMenu.key !== MainMenuType.STATISTICS,
// )

// export const orderCancelFilterTabList: FilterTab[] = [
//   {
//     key: FilterTabType.CANCEL,
//     icon: 'bag_cancel',
//     label: '취소',
//   },
//   {
//     key: FilterTabType.EXCHANGE,
//     icon: 'arrows_counter_clockwise',
//     label: '교환',
//   },
//   {
//     key: FilterTabType.RETURN,
//     icon: 'arrow_up_left',
//     label: '반품',
//   },
//   {
//     key: FilterTabType.REFUND,
//     icon: 'money',
//     label: '환불',
//   },
// ]

// export const orderDeliveryFilterTabList: FilterTab[] = [
//   {
//     key: FilterTabType.ORDER_RECEIVED,
//     icon: 'coin',
//     label: '주문 접수',
//   },
//   {
//     key: FilterTabType.PRODUCT_PREPARING,
//     icon: 'bag',
//     label: '상품 준비중',
//   },
//   {
//     key: FilterTabType.IN_DELIVERY,
//     icon: 'truck',
//     label: '배송 중',
//   },
//   {
//     key: FilterTabType.DELIVERED,
//     icon: 'package',
//     label: '배송 완료',
//   },
//   {
//     key: FilterTabType.ORDER_CONFIRMED,
//     icon: 'push_pin',
//     label: '구매 확정',
//   },
// ]

// export enum AtomFamilyKey {
//   SETTLEMENT_LIST = 'SETTLEMENT_LIST',
//   ADJUSTMENT_LIST = 'ADJUSTMENT_LIST',
//   NEED_REGISTER_LIST = 'NEED_REGISTER_LIST',
//   PAYMENT_LIST = 'PAYMENT_LIST',
//   TAX_BILL = 'TAX_BILL',
// }

// export const STORE_LAUNCHING_DATE = new Date('2022-04-06')
