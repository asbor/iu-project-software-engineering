export default function useHelpers() {
  let loading = ref(false);
  let open = ref(false);
  return {
    loading,
    open,
  };
}
