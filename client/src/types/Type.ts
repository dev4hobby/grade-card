import _ from 'lodash'

export enum type {
  ID = 'ID',
  Name = 'name',
  Priviliages = 'priviliages',
}

export interface IType {
  id: number
  name: string
  priviliages: JSON
}
