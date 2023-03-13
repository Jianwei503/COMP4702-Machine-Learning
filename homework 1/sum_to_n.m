function result = sum_to_n(arr, n)
    arr_length = length(arr)
    result = []
    % if the number of elements of the arr is less than 2,
    % not applicable for this function.
    if arr_length < 2
        return;
    end
    for i = 1:arr_length - 1
        for j = i + 1:arr_length
            if arr(i) + arr(j) == n
                result = [result; arr(i) arr(j)];
            end
        end
    end
end