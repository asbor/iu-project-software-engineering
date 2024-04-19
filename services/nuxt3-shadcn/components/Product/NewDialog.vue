<script setup lang="ts">
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from '@/components/ui/alert-dialog'

const { loading, open } = useHelpers();

const createNewProduct = () => {
  try {
    loading.value = true
    // all the business logic to create a new product
    console.log('Product created')
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
    open.value = false
    console.log('Product creation finished')
  }
}
</script>

<template>
  <AlertDialog :open="open">
    <Button @click="open = true">Add a new product</Button>
    <AlertDialogContent>
      <AlertDialogHeader>
        <AlertDialogTitle>Create a new product</AlertDialogTitle>
        <Input placeholder="Product name" />
      </AlertDialogHeader>
      <AlertDialogFooter>
        <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
        <AlertDialogAction @click="createNewProduct()">Create</AlertDialogAction>
      </AlertDialogFooter>
    </AlertDialogContent>
  </AlertDialog>
</template>