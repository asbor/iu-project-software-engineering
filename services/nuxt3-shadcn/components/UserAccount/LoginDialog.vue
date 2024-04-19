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

const login = () => {
    // TODO: Implement login logic
}
</script>

<template>
    <AlertDialog :open="open">
        <Button @click="open = true">Login</Button>
        <AlertDialogContent>
            <AlertDialogHeader>
                <AlertDialogTitle>Enter your username and password</AlertDialogTitle>
                <Input placeholder="Username" />
                <Input placeholder="Password" />
            </AlertDialogHeader>
            <AlertDialogFooter>
                <AlertDialogCancel @click="open = false">Cancel</AlertDialogCancel>
                <AlertDialogAction @click="login()">Login</AlertDialogAction>
            </AlertDialogFooter>
        </AlertDialogContent>
    </AlertDialog>
</template>