import _ from 'lodash'

export interface IUser {
  id: number
  name: string
  email: string
  alias: string
  phone: string
  createdAt: string
  updatedAt: string
  typeID: number
  schoolID: number
}

export enum user {
  ID = 'ID',
  Name = 'name',
  Email = 'email',
  Alias = 'alias',
  Phone = 'phone',
  CreatedAt = 'createdAt',
  UpdatedAt = 'updatedAt',
  TypeID = 'typeID',
  SchoolID = 'schoolID',
}
